// A lightweight fake-DOM smoke test. It is not a substitute for real browser testing.
const assert = require('assert');
const fs = require('fs');
const vm = require('vm');
const elements = new Map();
class Element {
  constructor(selector='') { this.selector=selector; this._html=''; this.textContent=''; this.value=''; this.dataset={}; this.style={setProperty(){}}; this.classList={toggle(){},add(){},remove(){}}; }
  set innerHTML(value) { this._html=value; }
  get innerHTML() { return this._html; }
  querySelectorAll(selector) { return dynamic(this._html,selector); }
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
const storage={}; const localStorage={getItem:k=>storage[k]??null,setItem:(k,v)=>{storage[k]=v}};
const courses=JSON.parse(fs.readFileSync('courses.json','utf8'));
const notes=JSON.parse(fs.readFileSync('prepared-notes.json','utf8'));
const fetch=async path=>({ok:true,json:async()=>path==='/courses.json'?courses:path==='/prepared-notes.json'?notes:{configured:false}});
const context=vm.createContext({document,localStorage,fetch,console,Date,setTimeout,window:{open(){},scrollTo(){}},navigator:{clipboard:{writeText:async()=>{}}},alert(){}});
vm.runInContext(fs.readFileSync('app.js','utf8'),context);
setImmediate(()=>{
 try {
  assert(el('#progressInfo').textContent.includes(`${Object.keys(notes).length} of ${courses.reduce((sum,c)=>sum+c.units.length,0)}`));
  assert(el('#preparedPicker').innerHTML.includes('Choose notes to read'));
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
  el('#surpriseBtn').onclick(); assert(el('#surpriseDialog').open);
  el('#textLarger').onclick(); assert.strictEqual(storage['ammu-reading-size'],'19');
  console.log('PASS: startup, Semester 5 subject/unit selection, preliminary badge, topic action, surprise and reading size (fake DOM)');
 } catch(err) { console.error(err);process.exitCode=1; }
});
