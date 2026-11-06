// Simulated service-worker and installation checks; not a real iOS/Android browser test.
const assert=require('assert'),fs=require('fs'),vm=require('vm');
(async()=>{
 const listeners={}, store=new Map(), origin='https://example.test';
 const key=r=>typeof r==='string'?new URL(r,origin).href:r.url;
 const cache={addAll:async urls=>urls.forEach(u=>store.set(key(u),new Response('cached '+u))),put:async(r,v)=>store.set(key(r),v),match:async r=>store.get(key(r))};
 let online=true;
 const self={location:{origin},clients:{claim:async()=>{}},addEventListener:(n,f)=>listeners[n]=f};
 const caches={open:async()=>cache,keys:async()=>['ammu-study-shell-old','unrelated'],delete:async k=>{assert.strictEqual(k,'ammu-study-shell-old');return true}};
 const context={self,caches,URL,Response,fetch:async()=>{if(!online)throw Error('offline');return new Response('fresh notes',{status:200})}};
 vm.runInNewContext(fs.readFileSync('sw.js','utf8'),context);
 let waiting;listeners.install({waitUntil:p=>waiting=p});await waiting;assert(store.has(origin+'/prepared-notes.json'));
 listeners.activate({waitUntil:p=>waiting=p});await waiting;
 const request=(path,mode='cors',method='GET')=>({url:origin+path,mode,method});
 let response;listeners.fetch({request:request('/prepared-notes.json'),respondWith:p=>response=p});assert.strictEqual(await (await response).text(),'fresh notes');
 online=false;listeners.fetch({request:request('/prepared-notes.json'),respondWith:p=>response=p});assert.strictEqual(await (await response).text(),'fresh notes');
 listeners.fetch({request:request('/', 'navigate'),respondWith:p=>response=p});assert.strictEqual((await response).status,200);
 let intercepted=false;listeners.fetch({request:request('/api/status'),respondWith:()=>intercepted=true});assert(!intercepted,'API must never be cached');
 const manifest=JSON.parse(fs.readFileSync('manifest.webmanifest','utf8'));assert.strictEqual(manifest.display,'standalone');assert(manifest.icons.some(i=>i.sizes==='192x192'));assert(manifest.icons.some(i=>i.sizes==='512x512'));
 for(const icon of manifest.icons)assert(fs.existsSync('.'+icon.src));
 // Test the manual iPhone installation help and registration scheduling.
 const nodes={};function node(k){return nodes[k]??=( {hidden:false,textContent:'',handlers:{},addEventListener(n,f){this.handlers[n]=f},showModal(){this.open=true},close(){this.open=false}} )}
 const handlers={};let registered='';
 const window={matchMedia:()=>({matches:false}),isSecureContext:true,addEventListener:(n,f)=>handlers[n]=f};
 const navigator={userAgent:'iPhone',platform:'iPhone',maxTouchPoints:5,serviceWorker:{register:p=>{registered=p;return Promise.resolve()}}};
 vm.runInNewContext(fs.readFileSync('pwa.js','utf8'),{document:{querySelector:node},window,navigator});
 await node('#installApp').handlers.click();assert(node('#installHelp').textContent.includes('Add to Home Screen'));assert(node('#installDialog').open);handlers.load();assert.strictEqual(registered,'/sw.js');
 console.log('PASS: simulated shell caching, offline fallback, API exclusion, manifest and iPhone installation help');
})().catch(e=>{console.error(e);process.exitCode=1});
