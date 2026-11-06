// A lightweight fake-DOM smoke test. It is not a substitute for real browser testing.
const assert = require('assert');
const fs = require('fs');
const vm = require('vm');
const elements = new Map();
class Element {
  constructor(selector='') { this.selector=selector; this._html=''; this.textContent=''; this.value=''; this.dataset={}; this.style={setProperty(){}}; this.classList={toggle(){},add(){},remove(){}}; }
  set innerHTML(value) { this._html=value; if(this.selector==='#chatBody') el('.chat-log').scrollTop=0; }
  get innerHTML() { return this._html; }
  querySelectorAll(selector) { this.childrenForTest=dynamic(this._html,selector); return this.childrenForTest; }
  querySelector(selector) { return el(this.selector+' '+selector); }
  getBoundingClientRect() { return {left:20,right:380,top:this.selector.startsWith('.chat-log [data-chat-reply=')?850:200,bottom:1000}; }
  setAttribute(name,value){ this[name]=value; }
  addEventListener(name,handler){(this.handlers||(this.handlers={}))[name]=handler;}
  scrollIntoView() {} showModal(){this.open=true} close(){this.open=false} insertAdjacentHTML(_,html){this._html+=html}
}
function el(key){ if(!elements.has(key)) elements.set(key,new Element(key)); return elements.get(key); }
function dynamic(html,sel) {
  const m=sel.match(/^\[data-(sem|topic|choice|saved)\]$/); if(!m)return [];
  return [...html.matchAll(new RegExp('data-'+m[1]+'="(\\d+)"','g'))].map(x=>{const node=new Element(); node.dataset[m[1]]=x[1]; return node;});
}
let topicButtons=[], semButtons=[], savedButtons=[];
const document={
  documentElement:el('root'),
  querySelector:s=>el(s),
  querySelectorAll:s=>{
    if(s==='[data-topic]') { topicButtons=dynamic(el('#preparedPicker').innerHTML,s); return topicButtons; }
    if(s==='[data-sem]') { semButtons=dynamic(el('#semTabs').innerHTML+el('#semesterNav').innerHTML,s); return semButtons; }
    if(s==='[data-saved]'){savedButtons=dynamic(el('#materialBody').innerHTML,s);return savedButtons;}
    if(s==='.material-tabs button')return ['notes','chat'].map(t=>{let e=new Element();e.dataset.tab=t;return e});
    return [];
  }
};
const storage={'marginalia-materials':JSON.stringify({'course-1:0':{plan:'A previously saved lesson plan'}}),'marginalia-saved':JSON.stringify([{courseId:'course-39',unitIndex:0,title:'Old semester 7 note',unit:'Unit 1',tab:'notes',key:'course-39:0'},{courseId:'course-1',unitIndex:0,title:'Semester 1 note',unit:'Unit 1',tab:'notes',key:'course-1:0'},{courseId:'course-1',unitIndex:0,title:'Previous plan',unit:'Unit 1',tab:'plan',key:'course-1:0'}])}; const localStorage={getItem:k=>storage[k]??null,setItem:(k,v)=>{storage[k]=v}};
const courses=JSON.parse(fs.readFileSync('courses.json','utf8'));
const notes=JSON.parse(fs.readFileSync('prepared-notes.json','utf8'));
let requestBody, failAI=false;
const fetch=async (path,options)=>{
 if(path==='/api/chat') { requestBody=JSON.parse(options.body); return failAI?{ok:false,status:503,json:async()=>({error:'Set AI_API_KEY in settings'})}:{ok:true,json:async()=>({text:'### A clear answer\n\n**Canterbury** is the destination.\n\n- First point\n- Second point'})}; }
 return {ok:true,json:async()=>path==='/courses.json'?courses:path==='/prepared-notes.json'?notes:{configured:false}};
};
const context=vm.createContext({document,localStorage,fetch,console,Date,setTimeout,window:{open(){},scrollTo(){}},navigator:{clipboard:{writeText:async()=>{}}},alert(){},confirm(){return true}});
vm.runInContext(fs.readFileSync('app.js','utf8'),context);
setImmediate(async ()=>{
 try {
  assert(el('#progressInfo').textContent.includes(`${Object.keys(notes).length} of ${courses.reduce((sum,c)=>sum+c.units.length,0)}`));
  assert(el('#preparedPicker').innerHTML.includes('Available topics'));
  const home=fs.readFileSync('index.html','utf8');
  assert(!home.includes('A note from us'));
  assert(!home.includes('id="setupDialog"')&&!home.includes('Connection instructions'));
  assert(!home.includes('data-tab="plan"')&&!home.includes('id="generatePlan"')&&!home.includes('id="durationChoice"'));
  assert(home.includes('data-tab="notes"')&&home.includes('data-tab="chat"'));
  assert(!home.includes('Notes are study drafts and may not yet cover every topic'));
  assert(!el('#progressInfo').textContent.includes('Many topics are still unfinished'));
  assert(!el('#materialMeta').textContent.includes('REVIEW BEFORE TEACHING'));
  assert(!Object.values(notes).flat().some(n=>n.text.split('\n').some(line=>line.startsWith('Teaching draft:'))));

  const tableHtml=vm.runInContext('md("| Heading | Value |\\n| --- | --- |\\n| &lt;safe&gt; | example |")', context);
  assert(tableHtml.includes('<table') && tableHtml.includes('<th scope="col">Heading</th>'));
  assert(!tableHtml.includes('<safe>'),'table cells must escape input');
  const rich = vm.runInContext('chatMarkdown('+JSON.stringify('### Example\n\n**Bold** and *italics*\n\n- first\n- second\n\n| Head | Meaning |\n| ---- | ---- |\n| item | first line\n- another detail |\n\n```\n<script>alert(1)</script>\n```')+')',context);
  assert(rich.includes('<h4>Example</h4>')&&rich.includes('<strong>Bold</strong>')&&rich.includes('<em>italics</em>'));
  assert(rich.includes('<ul><li>first</li><li>second</li></ul>')&&rich.includes('<table'));
  assert(rich.includes('first line<br>- another detail'),'multiline table cells are readable');
  assert(vm.runInContext('chatMarkdown('+JSON.stringify('Head | Meaning\n--- | ---\nA | B')+')',context).includes('<table'),'tables without outer pipes render');
  assert(!rich.includes('<script>')&&rich.includes('&lt;script&gt;'),'model output is escaped');
  const linkTest=vm.runInContext('chatMarkdown('+JSON.stringify('[bad](javascript:alert(1)) [good](https://example.com) <img src=x onerror=alert(1)>')+')',context);
  assert(!linkTest.includes('href="javascript:')&&!linkTest.includes('<img '));
  assert(linkTest.includes('href="https://example.com"'));

  semButtons.find(b=>b.dataset.sem==='3').onclick();
  el('#courseSelect').onchange({target:{value:'course-20'}});
  el('#unitSelect').onchange({target:{value:'4'}});
  assert(el('#materialBody').innerHTML.includes('<table class="note-table">'),'reported-speech tables render');
  semButtons.find(b=>b.dataset.sem==='1').onclick();
  assert(courses.every(c=>c.semester>=1&&c.semester<=6));
  assert(semButtons.some(b=>b.dataset.sem==='6'));
  assert(!semButtons.some(b=>+b.dataset.sem>6),'no semester 7 or 8 buttons');
  assert(!Object.keys(notes).some(k=>!courses.some(c=>k.startsWith(c.id+':'))),'all notes belong to retained courses');
  el('#savedNav').onclick();
  assert(!el('#materialBody').innerHTML.includes('Old semester 7 note'),'removed-course bookmark hidden');
  assert(el('#materialBody').innerHTML.includes('Semester 1 note'));
  assert.strictEqual(el('#savedCount').textContent,2);
  assert.strictEqual(JSON.parse(storage['marginalia-saved']).length,3,'older local data preserved');
  assert(el('#materialBody').innerHTML.includes('Previous plan'));
  savedButtons[1].onclick();
  assert(el('#materialBody').innerHTML.includes('A previously saved lesson plan'),'saved plan remains readable');
  assert(JSON.parse(storage['marginalia-materials'])['course-1:0'].plan,'saved plan data stays intact');
  el('#search').value='American Literature II'; el('#search').oninput();
  assert.strictEqual(el('#courseChoice').textContent,'No matching subjects');
  el('#search').value='';
  semButtons.find(b=>b.dataset.sem==='5').onclick();
  el('#courseSelect').onchange({target:{value:'course-27'}});
  assert(el('#courseChoice').textContent.includes('Literary Criticism'));
  assert(el('#materialBody').innerHTML.includes('Aristotle'));
  el('#unitSelect').onchange({target:{value:'3'}});
  assert(el('#preparedPicker').innerHTML.includes('INCOMPLETE'));
  assert(topicButtons[1] && topicButtons[1].onclick);
  topicButtons[1].onclick();
  assert(el('#materialMeta').textContent.includes('PRELIMINARY'));
  assert(el('#materialBody').innerHTML.includes('attribution'));
  // The same picker is used for subjects and units.
  for(const opener of ['#courseChoice','#unitChoice']) {
   el(opener).onclick(); const dialog=el('#choiceDialog'); assert(dialog.open);
   dialog.onclick({target:dialog,clientX:100,clientY:300}); assert(dialog.open,'inside padding must not close');
   dialog.onclick({target:el('#choiceList'),clientX:100,clientY:300}); assert(dialog.open,'inside content must not close');
   dialog.onclick({target:dialog,clientX:100,clientY:100}); assert(!dialog.open,'backdrop must close');
  }
  el('#unitChoice').onclick(); el('#choiceList').childrenForTest[1].onclick();
  assert(!el('#choiceDialog').open,'selection closes picker');
  assert.strictEqual(el('#unitSelect').value,'1','selection still changes unit');
  el('#unitChoice').onclick(); el('#closeChoice').onclick(); assert(!el('#choiceDialog').open,'close button still works');
  assert.strictEqual(el('#topicsView').hidden,false,'choosing unit opens topics screen');
  assert.strictEqual(el('#homeView').hidden,true);
  topicButtons[0].onclick();
  assert.strictEqual(el('#readingView').hidden,false,'selecting topic opens reading mode');
  assert.strictEqual(el('#topicsView').hidden,true);
  const readingBefore=el('#materialBody').innerHTML;
  el('#chatPanel').hidden=true;el('#openChat').onclick();
  assert.strictEqual(el('#chatPanel').hidden,false,'floating assistant opens');
  assert.strictEqual(el('#materialBody').innerHTML,readingBefore,'opening assistant preserves the note');
  vm.runInContext('busy=true;renderMaterial();busy=false',context);
  assert.strictEqual(el('#materialBody').innerHTML,readingBefore,'note remains readable while AI is busy');
  el('.chat-log').scrollHeight=2000;
  el('#chatInput').value='Explain this topic';
  await el('#chatForm').onsubmit({preventDefault(){}});
  assert(requestBody.messages.some(m=>m.content==='Explain this topic'),'Ask AI continues to work');
  assert(el('#chatBody').innerHTML.includes('<h4>A clear answer</h4>')&&el('#chatBody').innerHTML.includes('<strong>Canterbury</strong>'));
  assert(el('#chatBody').innerHTML.includes('data-copy-chat="1"'));
  assert(requestBody.messages[0].content.includes('one to three sentences'));
  assert(requestBody.messages[0].content.includes('meaning of a word or phrase'));
  assert(requestBody.messages[0].content.includes('Do not use emojis or decorative symbols'));
  const currentNote=notes[vm.runInContext('key()',context)][0];
  assert(requestBody.messages[0].content.includes(currentNote.title),'AI receives the selected topic');
  assert(requestBody.messages[0].content.includes(currentNote.text.slice(0,100)),'AI receives the reading note');
  assert(requestBody.messages[0].content.includes('detailed explanation when the user requests one'));
  assert(el('#chatBody').innerHTML.includes('data-chat-reply="1"'));
  assert.strictEqual(el('.chat-log').scrollTop,646,'new replies start at the top rather than the end');
  failAI=true;el('#chatInput').value='Another question';
  await el('#chatForm').onsubmit({preventDefault(){}});
  assert(!el('#chatError').innerHTML.includes('Connection setup'));
  assert(!el('#chatError').innerHTML.includes('AI_API_KEY'));
  assert(el('#chatError').textContent.includes('AI could not respond'));
  assert.strictEqual(el('#chatInput').value,'Another question','failed question remains available for retry');
  assert(!JSON.stringify(JSON.parse(storage['ammu-chat-history-v1'])).includes('Another question'),'failed messages are not saved');
  failAI=false;el('#chatInput').value='What did you just say?';
  await el('#chatForm').onsubmit({preventDefault(){}});
  assert(requestBody.messages.some(m=>m.role==='user'&&m.content==='Explain this topic'),'follow-up request includes earlier question');
  assert(requestBody.messages.some(m=>m.role==='assistant'&&m.content.includes('Canterbury')),'follow-up request includes earlier answer');
  const chatKey=vm.runInContext('key()',context), savedChats=JSON.parse(storage['ammu-chat-history-v1']);
  assert.strictEqual(savedChats[chatKey].length,4,'conversation is saved on this device');
  const reloaded=vm.createContext({document,localStorage,fetch,console,Date,setTimeout,window:{open(){},scrollTo(){}},navigator:{clipboard:{writeText:async()=>{}}},alert(){},confirm(){return true}});
  vm.runInContext(fs.readFileSync('app.js','utf8'),reloaded);
  await new Promise(resolve=>setImmediate(resolve));
  assert.strictEqual(vm.runInContext('chats['+JSON.stringify(chatKey)+'].length',reloaded),4,'history survives reload');
  vm.runInContext("course=courses.find(c=>c.id==='course-27');sem=5;unit=1;tab='chat';renderMaterial()",reloaded);
  assert(el('#chatBody').innerHTML.includes('What did you just say?'),'saved messages appear after reload');
  el('#unitSelect').onchange({target:{value:'2'}});
  vm.runInContext('renderChat()',reloaded);
  assert(!el('#chatBody').innerHTML.includes('What did you just say?'),'other units have separate chats');
  el('#unitSelect').onchange({target:{value:'1'}});
  vm.runInContext('renderChat()',reloaded);
  el('#clearChat').onclick();
  assert(!JSON.parse(storage['ammu-chat-history-v1'])[chatKey],'clear removes saved history for this unit');
  assert(!el('#chatBody').innerHTML.includes('What did you just say?'),'clear removes visible history');
  const capped=vm.runInContext('chatContext({role:"system",content:"context"},Array.from({length:20},()=>({role:"user",content:"x".repeat(12000)})))',reloaded);
  assert(JSON.stringify({messages:capped}).length<=56000,'long history stays under API request limit');


  el('#surpriseBtn').onclick(); assert(el('#surpriseDialog').open);
  el('#textLarger').onclick(); assert.strictEqual(storage['ammu-reading-size'],'19');
  const indexHtml = fs.readFileSync('index.html', 'utf8');
  assert(!indexHtml.includes('unit-details')&&!indexHtml.includes('generateNotes'),'unneeded final sections removed');
  assert(!indexHtml.includes('sky-cloud')&&!indexHtml.includes('heart-icon'),'decorative imagery removed');
  assert(indexHtml.includes('id="sourceBtn"')&&indexHtml.includes('id="chatWidget"'),'source and AI remain available');
  console.log('PASS: startup, topic selection, backdrop dismissal, close button, picker selection, surprise and reading size (fake DOM)');
 } catch(err) { console.error(err);process.exitCode=1; }
});
