// A lightweight fake-DOM smoke test. It is not a substitute for real browser testing.
const assert = require('assert');
const fs = require('fs');
const vm = require('vm');
const elements = new Map();
class Element {
  constructor(selector='') { this.selector=selector; this._html=''; this.textContent=''; this.value=''; this.dataset={}; this.style={setProperty(){}}; this.classList={toggle(){},add(){},remove(){}}; }
  set innerHTML(value) { this._html=value; }
  get innerHTML() { return this._html; }
  querySelectorAll(selector) { this.childrenForTest=dynamic(this._html,selector); return this.childrenForTest; }
  getBoundingClientRect() { return {left:20,right:380,top:200,bottom:700}; }
  setAttribute(name,value){ this[name]=value; }
  scrollIntoView() {} showModal(){this.open=true} close(){this.open=false} insertAdjacentHTML(_,html){this._html+=html}
}
function el(key){ if(!elements.has(key)) elements.set(key,new Element(key)); return elements.get(key); }
function dynamic(html,sel) {
  const m=sel.match(/^\[data-(sem|topic|choice|saved)\]$/); if(!m)return [];
  return [...html.matchAll(new RegExp('data-'+m[1]+'="(\\d+)"','g'))].map(x=>{const node=new Element(); node.dataset[m[1]]=x[1]; return node;});
}
let topicButtons=[], semButtons=[];
const document={
  documentElement:el('root'),
  querySelector:s=>el(s),
  querySelectorAll:s=>{
    if(s==='[data-topic]') { topicButtons=dynamic(el('#preparedPicker').innerHTML,s); return topicButtons; }
    if(s==='[data-sem]') { semButtons=dynamic(el('#semTabs').innerHTML+el('#semesterNav').innerHTML,s); return semButtons; }
    if(s==='.material-tabs button')return ['notes','plan','chat'].map(t=>{let e=new Element();e.dataset.tab=t;return e});
    return [];
  }
};
const storage={'marginalia-saved':JSON.stringify([{courseId:'course-39',unitIndex:0,title:'Old semester 7 note',unit:'Unit 1',tab:'notes',key:'course-39:0'},{courseId:'course-1',unitIndex:0,title:'Semester 1 note',unit:'Unit 1',tab:'notes',key:'course-1:0'}])}; const localStorage={getItem:k=>storage[k]??null,setItem:(k,v)=>{storage[k]=v}};
const courses=JSON.parse(fs.readFileSync('courses.json','utf8'));
const notes=JSON.parse(fs.readFileSync('prepared-notes.json','utf8'));
const fetch=async path=>({ok:true,json:async()=>path==='/courses.json'?courses:path==='/prepared-notes.json'?notes:{configured:false}});
const context=vm.createContext({document,localStorage,fetch,console,Date,setTimeout,window:{open(){},scrollTo(){}},navigator:{clipboard:{writeText:async()=>{}}},alert(){}});
vm.runInContext(fs.readFileSync('app.js','utf8'),context);
setImmediate(()=>{
 try {
  assert(el('#progressInfo').textContent.includes(`${Object.keys(notes).length} of ${courses.reduce((sum,c)=>sum+c.units.length,0)}`));
  assert(el('#preparedPicker').innerHTML.includes('Choose notes to read'));
  const tableHtml=vm.runInContext('md("| Heading | Value |\\n| --- | --- |\\n| &lt;safe&gt; | example |")', context);
  assert(tableHtml.includes('<table') && tableHtml.includes('<th scope="col">Heading</th>'));
  assert(!tableHtml.includes('<safe>'),'table cells must escape input');
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
  assert.strictEqual(el('#savedCount').textContent,1);
  assert.strictEqual(JSON.parse(storage['marginalia-saved']).length,2,'older local data preserved');
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
  // The same picker is used for subjects, units and durations.
  for(const opener of ['#courseChoice','#unitChoice','#durationChoice']) {
   el(opener).onclick(); const dialog=el('#choiceDialog'); assert(dialog.open);
   dialog.onclick({target:dialog,clientX:100,clientY:300}); assert(dialog.open,'inside padding must not close');
   dialog.onclick({target:el('#choiceList'),clientX:100,clientY:300}); assert(dialog.open,'inside content must not close');
   dialog.onclick({target:dialog,clientX:100,clientY:100}); assert(!dialog.open,'backdrop must close');
  }
  el('#unitChoice').onclick(); el('#choiceList').childrenForTest[1].onclick();
  assert(!el('#choiceDialog').open,'selection closes picker');
  assert.strictEqual(el('#unitSelect').value,'1','selection still changes unit');
  el('#unitChoice').onclick(); el('#closeChoice').onclick(); assert(!el('#choiceDialog').open,'close button still works');
  el('#surpriseBtn').onclick(); assert(el('#surpriseDialog').open);
  el('#textLarger').onclick(); assert.strictEqual(storage['ammu-reading-size'],'19');
  console.log('PASS: startup, topic selection, backdrop dismissal, close button, picker selection, surprise and reading size (fake DOM)');
 } catch(err) { console.error(err);process.exitCode=1; }
});
