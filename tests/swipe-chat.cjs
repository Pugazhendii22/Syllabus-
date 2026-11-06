// Real Chromium touch events in phone emulation; no physical-device or live-AI test.
const {chromium}=require('playwright');
const assert=require('assert');
const fs=require('fs');
const base=process.env.AMMU_TEST_URL||'http://127.0.0.1:8000';
const sizes=[{name:'small-phone',width:320,height:568},{name:'phone',width:390,height:844},{name:'landscape',width:568,height:320}];
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 try{
  for(const size of sizes){
   const context=await browser.newContext({viewport:{width:size.width,height:size.height},isMobile:true,hasTouch:true,serviceWorkers:'block'}),page=await context.newPage();
   const cdp=await context.newCDPSession(page);let navigations=0;
   page.on('framenavigated',frame=>{if(frame===page.mainFrame())navigations++});
   await page.route('**/api/chat',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({text:'### Explanation\n\n'+('This is a long answer to read. '.repeat(100))})}));
   async function drag(target,points){
    const box=await target.boundingBox(),x=box.x+box.width/2,y=box.y+Math.min(15,box.height/2);
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y}]});
    for(const [dx,dy] of points)await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:x+dx,y:y+dy}]});
    await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
   }
   try{
    await page.goto(base);await page.waitForFunction(()=>document.querySelectorAll('[data-topic]').length);
    await page.locator('#openTopics').tap();await page.locator('#preparedPicker [data-topic]').first().tap();
    await page.locator('#openChat').tap();assert(await page.locator('.chat-swipe-hint').isVisible());
    await page.locator('#chatInput').fill('My unsent question');
    const hint=page.locator('.chat-swipe-hint');
    await drag(hint,[[0,20],[0,35]]);assert(await page.locator('#chatPanel').isVisible(),'short drag must not close');
    await drag(hint,[[30,4],[90,12]]);assert(await page.locator('#chatPanel').isVisible(),'horizontal drag must not close');
    await drag(hint,[[0,30],[0,90],[0,5]]);assert(await page.locator('#chatPanel').isVisible(),'dragging back should cancel closing');
    await drag(page.locator('#closeChat'),[[0,25],[0,110]]);assert(await page.locator('#chatPanel').isVisible(),'dragging from a button must not trigger swipe-to-close');
    const before=navigations;
    await drag(hint,[[0,25],[0,50],[0,75],[0,105]]);
    assert(await page.locator('#chatPanel').isHidden(),'downward swipe closes chat');
    assert(await page.locator('#readingView').isVisible(),'reading remains open');
    assert.equal(navigations,before,'swipe must not trigger pull-to-refresh');
    assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('ammu-navigation-v1')).chatOpen),false,'closed state is saved');
    await page.locator('#openChat').tap();assert.equal(await page.locator('#chatInput').inputValue(),'My unsent question','draft survives swipe close');
    await page.locator('.chat-send').tap();await page.locator('.chat-rich').waitFor();
    const log=page.locator('.chat-log');await log.evaluate(node=>node.scrollTop=200);
    assert((await log.evaluate(node=>node.scrollTop))>1,'test conversation is scrollable');
    await drag(log,[[0,25],[0,50],[0,75],[0,105]]);
    assert(await page.locator('#chatPanel').isVisible(),'scrolling a reply must not close chat');
    await log.evaluate(node=>node.scrollTop=0);await drag(log,[[0,25],[0,50],[0,75],[0,105]]);
    assert(await page.locator('#chatPanel').isHidden(),'swiping down from the top of the conversation closes chat');
    await page.locator('#openChat').tap();assert((await page.locator('#chatBody').textContent()).includes('This is a long answer'),'saved conversation survives closing');
    console.log('PASS swipe',size.name,`${size.width}x${size.height}`,'short, horizontal, controls, scroll, draft and conversation');
   }catch(error){fs.mkdirSync('test-results',{recursive:true});const path=`test-results/swipe-${size.name}.png`;await page.screenshot({path,fullPage:true}).catch(()=>{});console.error('Failure screenshot:',path);throw error}
   finally{await context.close()}
  }
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
