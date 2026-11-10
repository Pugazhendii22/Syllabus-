// Real Chromium touch gestures in emulated phones, not a physical-device test.
const {chromium}=require('playwright');
const assert=require('assert');
const base=process.env.AMMU_TEST_URL||'http://127.0.0.1:8000';
const sizes=[{name:'small-phone',width:320,height:568},{name:'phone',width:390,height:844},{name:'landscape',width:568,height:320}];
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 try{for(const size of sizes){
  const context=await browser.newContext({viewport:{width:size.width,height:size.height},isMobile:true,hasTouch:true,serviceWorkers:'block'});
  const page=await context.newPage(),cdp=await context.newCDPSession(page),errors=[];page.on('pageerror',e=>errors.push(e.message));
  async function dragXY(x,y,dx,dy=0){
   await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y}]});
   for(const n of [0.2,0.5,0.8,1])await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:x+dx*n,y:y+dy*n}]});
   await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
  }
  async function dragHeader(dx,dy=0){
   await page.locator('.material-head').scrollIntoViewIfNeeded();
   const box=await page.locator('.material-head').boundingBox();
   await dragXY(size.width/2,Math.max(10,box.y+16),dx,dy);
  }
  const position=()=>page.locator('#topicPosition').textContent();
  try{
   await page.goto(base);await page.waitForFunction(()=>document.querySelectorAll('[data-topic]').length>0);
   await page.locator('#openTopics').tap();await page.locator('#preparedPicker [data-topic]').first().tap();
   assert(await page.locator('#topicSwipeHint').isVisible(),'hint shown on touch devices');
   assert.equal(await position(),'Topic 1 of 4');
   await dragHeader(110);assert.equal(await position(),'Topic 1 of 4','previous at first topic must not wrap');
   await dragHeader(-35);assert.equal(await position(),'Topic 1 of 4','short gesture must not navigate');
   // Browser back/forward gestures near the edge are left alone.
   await page.locator('.material-head').scrollIntoViewIfNeeded();
   const edgeBox=await page.locator('.material-head').boundingBox();await dragXY(20,edgeBox.y+16,110);
   assert.equal(await position(),'Topic 1 of 4','edge gestures must not change topics');
   // A second finger cancels topic navigation.
   const mh=await page.locator('.material-head').boundingBox(),mx=size.width/2,my=mh.y+16;
   await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:mx,y:my,id:1}]});
   await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:mx,y:my,id:1},{x:mx+20,y:my,id:2}]});
   await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:mx-110,y:my,id:1},{x:mx-90,y:my,id:2}]});
   await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
   assert.equal(await position(),'Topic 1 of 4','multi-touch must not navigate');
   await dragHeader(-100,90);assert.equal(await position(),'Topic 1 of 4','diagonal scrolling must not navigate');
   await dragHeader(-110);assert.equal(await position(),'Topic 2 of 4','left goes to next');
   assert((await page.locator('#readingTitle').textContent()).includes('Spenser'));
   assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('ammu-navigation-v1')).topicIndex),1,'new topic is saved');
   await page.reload();await page.waitForFunction(()=>document.querySelector('#topicPosition').textContent==='Topic 2 of 4');
   await dragHeader(110);assert.equal(await position(),'Topic 1 of 4','right goes to previous');
   await page.evaluate(()=>window.scrollTo(0,700));
   await page.waitForFunction(()=>window.scrollY>100);
   const middle=await page.evaluate(({w,h})=>{const x=w/2,y=h/2,e=document.elementFromPoint(x,y);return {x,y,inside:!!e?.closest('#materialBody'),tag:e?.tagName}}, {w:size.width,h:size.height});
   assert(middle.inside,`gesture begins on note text: ${JSON.stringify(middle)}`);
   await dragXY(middle.x,middle.y,-110);
   assert.equal(await position(),'Topic 2 of 4','swipe within note text moves to next topic');
   assert((await page.evaluate(()=>window.scrollY))<5,'new topic opens at the top');
   await dragHeader(110);assert.equal(await position(),'Topic 1 of 4');
   // Buttons are not a swipe surface and remain usable.
   const button=await page.locator('#saveBtn').boundingBox();await dragXY(button.x+button.width/2,button.y+button.height/2,-110);
   assert.equal(await position(),'Topic 1 of 4','swipes from controls are ignored');
   await page.locator('#nextTopic').scrollIntoViewIfNeeded();await page.locator('#nextTopic').tap();assert.equal(await position(),'Topic 2 of 4','next button still works');
   // A selection must not be discarded by a topic swipe.
   await page.locator('#readingTitle').scrollIntoViewIfNeeded();await page.evaluate(()=>{const node=document.querySelector('#readingTitle').firstChild,r=document.createRange();r.setStart(node,0);r.setEnd(node,5);const s=getSelection();s.removeAllRanges();s.addRange(r)});
   await dragHeader(-110);assert.equal(await position(),'Topic 2 of 4','text selection blocks navigation');
   await page.evaluate(()=>getSelection().removeAllRanges());
   await page.emulateMedia({reducedMotion:'reduce'});await dragHeader(-110);assert.equal(await position(),'Topic 3 of 4');
   assert.equal(await page.locator('.materials').evaluate(e=>getComputedStyle(e).animationName),'none','reduced motion disables transition');
   await page.emulateMedia({reducedMotion:'no-preference'});await dragHeader(-110);assert.equal(await position(),'Topic 4 of 4');
   await dragHeader(-110);assert.equal(await position(),'Topic 4 of 4','next at last topic must not wrap');
   // The chat panel is independent, and its horizontal gestures cannot change the note.
   await page.locator('#openChat').tap();const hint=await page.locator('.chat-swipe-hint').boundingBox();
   await dragXY(size.width/2,hint.y+hint.height/2,-110);assert(await page.locator('#chatPanel').isVisible());assert.equal(await position(),'Topic 4 of 4');
   await page.locator('#closeChat').click();assert(await page.locator('#chatPanel').isHidden());
   // A horizontal table swipe scrolls the table, even at the boundary, not the topic.
   await page.locator('#brandHome').click();await page.locator('#courseChoice').click();
   await page.locator('#choiceList button').filter({hasText:'Spoken English'}).click();await page.locator('#unitChoice').click();await page.locator('#choiceList button').nth(1).click();
   await page.locator('#preparedPicker [data-topic]').filter({hasText:'Original PDF notes'}).click();
   const before=await position(),table=page.locator('.note-table-wrap').first();await table.scrollIntoViewIfNeeded();
   const tb=await table.boundingBox(),y=Math.max(10,Math.min(size.height-10,tb.y+Math.min(tb.height/2,40)));
   await dragXY(Math.min(size.width-35,tb.x+tb.width-30),y,-110);
   assert.equal(await position(),before,'table swipe must not change topics');
   assert((await table.evaluate(el=>el.scrollLeft))>0,'table remains horizontally scrollable');
   assert.equal(errors.length,0,errors.join('\n'));
   console.log('PASS topic swipes',size.name,'directions, boundaries, selection, controls, reload, chat and table');
  }finally{await context.close()}
 }}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
