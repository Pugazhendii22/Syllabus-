// Simulated service-worker and installation checks; not a real iOS/Android browser test.
const assert=require('assert'),fs=require('fs'),vm=require('vm');
(async()=>{
 const listeners={}, store=new Map(), origin='https://example.test';
 const key=r=>typeof r==='string'?new URL(r,origin).href:r.url;
 const cache={addAll:async urls=>urls.forEach(u=>store.set(key(u),new Response('cached '+u))),put:async(r,v)=>store.set(key(r),v),match:async r=>store.get(key(r))};
 let online=true;
 let skipped=false; const self={location:{origin},clients:{claim:async()=>{}},skipWaiting:()=>{skipped=true},addEventListener:(n,f)=>listeners[n]=f};
 const caches={open:async()=>cache,keys:async()=>['ammu-study-shell-old','unrelated'],delete:async k=>{assert.strictEqual(k,'ammu-study-shell-old');return true}};
 const context={self,caches,URL,Response,fetch:async()=>{if(!online)throw Error('offline');return new Response('fresh notes',{status:200})}};
 vm.runInNewContext(fs.readFileSync('sw.js','utf8'),context);
 let waiting;listeners.install({waitUntil:p=>waiting=p});await waiting;assert(store.has(origin+'/prepared-notes.json'));
 listeners.activate({waitUntil:p=>waiting=p});await waiting;
 listeners.message({data:{type:'IGNORED'}});assert(!skipped);listeners.message({data:{type:'SKIP_WAITING'}});assert(skipped);
 const request=(path,mode='cors',method='GET')=>({url:origin+path,mode,method});
 let response;listeners.fetch({request:request('/prepared-notes.json'),respondWith:p=>response=p});assert.strictEqual(await (await response).text(),'fresh notes');
 online=false;listeners.fetch({request:request('/prepared-notes.json'),respondWith:p=>response=p});assert.strictEqual(await (await response).text(),'fresh notes');
 listeners.fetch({request:request('/', 'navigate'),respondWith:p=>response=p});assert.strictEqual((await response).status,200);
 let intercepted=false;listeners.fetch({request:request('/api/status'),respondWith:()=>intercepted=true});assert(!intercepted,'API must never be cached');
 const manifest=JSON.parse(fs.readFileSync('manifest.webmanifest','utf8'));assert.strictEqual(manifest.display,'standalone');assert(manifest.icons.some(i=>i.sizes==='192x192'));assert(manifest.icons.some(i=>i.sizes==='512x512'));
 for(const icon of manifest.icons)assert(fs.existsSync('.'+icon.src));
 // Simulate update lifecycle, user consent, and mobile pull gestures.
 const nodes={};function node(k){return nodes[k]??=( {hidden:k==='#updateNotice'||k==='#pullStatus',value:'',textContent:'',handlers:{},addEventListener(n,f){this.handlers[n]=f},showModal(){this.open=true},close(){this.open=false}} )}
 const dh={},wh={},sh={};let registered='',reloads=0,asked=0,confirmed=true,posted=[];
 const registration={waiting:null,installing:null,handlers:{},update:async()=>{},addEventListener(n,f){this.handlers[n]=f}};
 const window={matchMedia:()=>({matches:false}),isSecureContext:true,scrollY:0,location:{reload(){reloads++}},getComputedStyle:()=>({overflowY:'visible'}),confirm(){asked++;return confirmed},setTimeout(){},setInterval(){},addEventListener:(n,f)=>wh[n]=f};
 const navigator={userAgent:'iPhone',platform:'iPhone',maxTouchPoints:5,serviceWorker:{controller:{},handlers:sh,register:(p,opts)=>{registered=p;assert.strictEqual(opts.updateViaCache,'none');return Promise.resolve(registration)},addEventListener(n,f){sh[n]=f}}};
 const body={},root={};const document={body,documentElement:root,hidden:false,querySelector:s=>s==='dialog[open]'?null:node(s),addEventListener:(n,f)=>dh[n]=f};
 vm.runInNewContext(fs.readFileSync('pwa.js','utf8'),{document,window,navigator});
 await node('#installApp').handlers.click();assert(node('#installHelp').textContent.includes('Add to Home Screen'));assert(node('#installDialog').open);
 wh.load();await Promise.resolve();assert.strictEqual(registered,'/sw.js');assert(node('#updateNotice').hidden,'first install should not show notice without waiting update');
 const worker={state:'installing',handlers:{},addEventListener(n,f){this.handlers[n]=f},postMessage:m=>posted.push(m.type)};
 registration.installing=worker;registration.handlers.updatefound();registration.waiting=worker;worker.state='installed';worker.handlers.statechange();assert(!node('#updateNotice').hidden,'new worker shows notice');
 node('#laterUpdate').handlers.click();assert(node('#updateNotice').hidden);dh.visibilitychange();assert(!node('#updateNotice').hidden);
 node('#topicInput').value='unsent';confirmed=false;node('#reloadUpdate').handlers.click();assert.strictEqual(asked,1);assert.strictEqual(posted.length,0);assert.strictEqual(reloads,0);
 confirmed=true;node('#reloadUpdate').handlers.click();assert.deepStrictEqual(posted,['SKIP_WAITING']);assert.strictEqual(reloads,0);sh.controllerchange();sh.controllerchange();assert.strictEqual(reloads,1,'reload once after activation');
 // Separate runtime to check touch thresholds, cancellation and nested content.
 function pullRuntime(){
  const events={},els={},win={...window,location:{reload(){reloads++}},scrollY:0,addEventListener(){},getComputedStyle:n=>({overflowY:n.overflowY||'visible'})};
  const doc={body,documentElement:root,hidden:false,querySelector:s=>s==='dialog[open]'?null:(els[s]??=( {hidden:true,value:'',textContent:'',handlers:{},addEventListener(n,f){this.handlers[n]=f}} )),addEventListener:(n,f)=>events[n]=f};
  vm.runInNewContext(fs.readFileSync('pwa.js','utf8'),{document:doc,window:win,navigator:{userAgent:'',platform:'',maxTouchPoints:0}});
  return {events,els,win};
 }
 const {events,els,win}=pullRuntime();const target={parentElement:body,scrollHeight:10,clientHeight:10,closest:()=>null};
 const touch=y=>({target,touches:[{clientX:0,clientY:y}],cancelable:true,preventDefault(){this.prevented=true}});
 let before=reloads;events.touchstart(touch(0));events.touchmove(touch(50));events.touchend();assert.strictEqual(reloads,before);
 events.touchstart(touch(0));let move=touch(120);events.touchmove(move);assert(move.prevented);assert(els['#pullStatus'].textContent.includes('Release'));events.touchend();assert.strictEqual(reloads,before+1);
 const rt=pullRuntime();const scroller={...target,overflowY:'auto',scrollHeight:500,clientHeight:100};const nested={...target,parentElement:scroller};rt.events.touchstart({...touch(0),target:nested});rt.events.touchmove(touch(150));rt.events.touchend();assert.strictEqual(reloads,before+1,'nested scroll must not refresh');
 const another=pullRuntime();another.events.touchstart(touch(0));another.events.touchmove(touch(120));another.events.touchcancel();another.events.touchend();assert.strictEqual(reloads,before+1,'cancelled gesture must not refresh');
 console.log('PASS: simulated offline shell, update notice/activation, unsent text protection, pull gesture, nested scrolling and iPhone installation help');
})().catch(e=>{console.error(e);process.exitCode=1});
