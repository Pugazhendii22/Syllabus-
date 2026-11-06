// Automated Chromium phone emulation; AI responses are mocked. This is not a physical-device test.
const {chromium}=require('playwright');
const assert=require('assert');
const fs=require('fs');
const base=process.env.AMMU_TEST_URL || 'http://127.0.0.1:8000';
const sizes=[
 {name:'small-phone',width:320,height:568,mobile:true},
 {name:'android-phone',width:360,height:640,mobile:true},
 {name:'phone',width:390,height:844,mobile:true},
 {name:'large-phone',width:430,height:932,mobile:true},
 {name:'phone-landscape',width:568,height:320,mobile:true},
 {name:'large-phone-landscape',width:852,height:393,mobile:true},
 {name:'wide-phone-landscape',width:932,height:430,mobile:true},
 {name:'desktop',width:1440,height:900,mobile:false}
];
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 try{
  for(const size of sizes){
   const context=await browser.newContext({viewport:{width:size.width,height:size.height},deviceScaleFactor:1,isMobile:size.mobile,hasTouch:size.mobile,serviceWorkers:'block'});
   const page=await context.newPage(), errors=[], requests=[];
   const activate=locator=>size.mobile?locator.tap():locator.click();
   page.on('pageerror',error=>errors.push(error.message));
   await page.route('**/api/chat',async route=>{requests.push(route.request().postDataJSON());await route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({text:'### Answer\n\nA **brief explanation**.\n\n'+('A longer explanation for reading. '.repeat(120))})})});
   const noHorizontalOverflow=async stage=>{
    const dimensions=await page.evaluate(()=>({doc:document.documentElement.scrollWidth,view:window.innerWidth}));
    assert(dimensions.doc<=dimensions.view,`${stage} overflows horizontally: ${JSON.stringify(dimensions)}`);
   };
   try{
    await page.goto(base);await page.waitForFunction(()=>document.querySelector('#courseChoice').textContent.includes('English Literature'));
    assert(await page.locator('#homeView').isVisible());assert(!(await page.locator('#topicsView').isVisible()));await noHorizontalOverflow('home');
    assert.equal(await page.locator('.home-cloud').count(),2,'home has passing background clouds');
    const cloudStyle=await page.locator('.home-cloud-layer').evaluate(el=>({position:getComputedStyle(el).position,events:getComputedStyle(el).pointerEvents,z:getComputedStyle(el).zIndex}));
    assert.deepStrictEqual(cloudStyle,{position:'absolute',events:'none',z:'0'},'clouds are behind content and occupy no layout space');
    assert.equal(await page.locator('.cloud-one').evaluate(el=>getComputedStyle(el).animationName),'home-cloud-pass','clouds move');
    await page.emulateMedia({reducedMotion:'reduce'});
    assert.equal(await page.locator('.cloud-one').evaluate(el=>getComputedStyle(el).animationName),'none','cloud movement respects reduced motion');
    await page.emulateMedia({reducedMotion:'no-preference'});
    await page.locator('#homeHeading').focus();
    const headingFocus=await page.locator('#homeHeading').evaluate(el=>({style:getComputedStyle(el).outlineStyle,width:getComputedStyle(el).outlineWidth,radius:getComputedStyle(el).borderRadius}));
    assert.deepStrictEqual(headingFocus,{style:'solid',width:'2px',radius:'3px'},'home heading uses a consistent rectangular focus outline');
    await page.locator('#search').focus();
    const searchFocus=await page.locator('#search').evaluate(el=>({input:getComputedStyle(el).outlineStyle,wrapper:getComputedStyle(el.parentElement).outlineStyle,width:getComputedStyle(el.parentElement).outlineWidth,radius:getComputedStyle(el.parentElement).borderRadius}));
    assert.deepStrictEqual(searchFocus,{input:'none',wrapper:'solid',width:'3px',radius:'12px'},'search focus is visible on its rounded container');
    assert(await page.locator('#refreshApp').isVisible(),'refresh remains available on the home screen');
    assert(await page.locator('footer #sourceBtn').isVisible() && await page.locator('footer #progressInfo').isVisible(),'PDF and section count are in the home footer');
    assert.equal(await page.locator('.selection-card #sourceBtn, .selection-card #progressInfo').count(),0,'secondary items are not in the selection card');
    const refresh=await page.locator('#refreshApp').boundingBox(),savedButton=await page.locator('#mobileSaved').boundingBox();
    assert(Math.abs((refresh.y+refresh.height/2)-(savedButton.y+savedButton.height/2))<2,'home header controls are vertically aligned');
    if(size.width<=480){
     const icon=await page.locator('#refreshApp .refresh-icon').boundingBox();
     assert(Math.abs(refresh.width-refresh.height)<0.1,'mobile refresh button is circular');
     assert(Math.abs((icon.x+icon.width/2)-(refresh.x+refresh.width/2))<0.5 && Math.abs((icon.y+icon.height/2)-(refresh.y+refresh.height/2))<0.5,'refresh icon is centred inside its button');
    }
    assert(!/[↗→←]/.test(await page.locator('#sourceBtn').textContent()));assert(!/[↗→←]/.test(await page.locator('#openTopics').textContent()));
    if(size.mobile){
     const bounds=await page.locator('#semTabs').evaluate(el=>({parent:el.getBoundingClientRect().toJSON(),buttons:[...el.querySelectorAll('button')].map(b=>b.getBoundingClientRect().toJSON())}));
     assert.equal(bounds.buttons.length,6);
     assert(bounds.buttons.every(b=>b.left>=bounds.parent.left-1&&b.right<=bounds.parent.right+1),'all semesters are visible without horizontal scrolling');
    }
    await activate(page.locator('#semTabs [data-sem="3"]'));await activate(page.locator('#courseChoice'));
    await activate(page.locator('#choiceList button').filter({hasText:'Functional English Ii'}));
    await Promise.all([page.waitForEvent('load'),activate(page.locator('#refreshApp'))]);
    await page.waitForFunction(()=>document.querySelector('#courseChoice').textContent.includes('Functional English Ii'));
    assert(await page.locator('#homeView').isVisible(),'refresh button retains the home screen and selected subject');
    await page.evaluate(()=>{window.__openedPdf='';window.open=url=>{window.__openedPdf=url}});await activate(page.locator('#sourceBtn'));
    const selectedPage=await page.evaluate(async()=>{const c=await (await fetch('/courses.json')).json();return c.find(x=>x.title.toLowerCase()==='functional english ii').page});
    assert((await page.evaluate(()=>window.__openedPdf)).endsWith('#page='+selectedPage),'footer PDF opens at selected subject page');
    await activate(page.locator('#unitChoice'));await activate(page.locator('#choiceList button').nth(1));
    assert(await page.locator('#topicsView').isVisible());assert(!(await page.locator('#homeView').isVisible()));await noHorizontalOverflow('topics');
    assert(!(await page.locator('.home-cloud-layer').isVisible()),'cloud stays on home only');
    assert(!(await page.locator('#homeFooterDetails').isVisible()),'home footer details are hidden on other screens');
    assert(!(await page.locator('#refreshApp').isVisible()),'refresh is not repeated on the topics screen');
    assert.equal(await page.locator('#preparedPicker [data-topic]').count(),3);
    await page.reload();
    await page.waitForFunction(()=>!document.querySelector('#topicsView').hidden);
    assert.equal(await page.locator('#preparedPicker [data-topic]').count(),3,'refresh retains the selected unit and topics screen');
    assert.equal(await page.locator('#topicsHeading').evaluate(el=>{el.focus({preventScroll:true});return getComputedStyle(el).outlineStyle}),'none','topics heading has no focus outline after refresh');
    await activate(page.locator('#preparedPicker [data-topic]').first());
    assert(await page.locator('#readingView').isVisible());assert(!(await page.locator('#topicsView').isVisible()));await noHorizontalOverflow('reading');
    if(size.mobile && size.width>size.height && size.height<=500)assert(!(await page.locator('.sidebar').isVisible()),'sidebar is hidden in phone landscape reading mode');
    if(!size.mobile)assert(await page.locator('.sidebar').isVisible(),'desktop sidebar remains visible');
    assert(!(await page.locator('#refreshApp').isVisible()),'refresh is not repeated in reading mode');
    assert((await page.locator('#readingTitle').textContent()).includes('Cow'));
    await page.evaluate(()=>window.scrollTo(0,900));
    await page.waitForFunction(()=>{try{return JSON.parse(localStorage.getItem('ammu-navigation-v1')).scrollY>400}catch{return false}});
    const originalScroll=await page.evaluate(()=>window.scrollY);
    await page.evaluate(()=>{const saved=JSON.parse(localStorage.getItem('ammu-navigation-v1'));saved.topicIndex=999;localStorage.setItem('ammu-navigation-v1',JSON.stringify(saved))});
    await page.reload();
    await page.waitForFunction(()=>!document.querySelector('#readingView').hidden&&document.querySelector('#readingTitle').textContent.includes('Cow'));
    // Mobile layout and browser scroll anchoring can shift the position slightly during reload.
    await page.waitForFunction(y=>Math.abs(window.scrollY-y)<100,originalScroll);
    assert.equal(await page.locator('#readingTitle').evaluate(el=>{el.focus({preventScroll:true});return getComputedStyle(el).outlineStyle}),'none','reading heading has no focus outline after refresh');
    assert((await page.locator('#topicPosition').textContent()).includes('1 of 3'));
    assert(await page.locator('#previousTopic').isDisabled());
    await activate(page.locator('#nextTopic'));
    assert((await page.locator('#readingTitle').textContent()).includes('Beauty Industry'));
    assert((await page.locator('#topicPosition').textContent()).includes('2 of 3'));
    await activate(page.locator('#previousTopic'));
    assert((await page.locator('#readingTitle').textContent()).includes('Cow'));
    assert(await page.locator('#openChat').isVisible());
    const fab=await page.locator('#openChat').boundingBox();assert(fab.y>=0&&fab.y+fab.height<=size.height,'floating assistant stays within viewport');
    const before=await page.locator('#materialBody').textContent();await activate(page.locator('#openChat'));
    assert.equal(await page.locator('#materialBody').textContent(),before);await noHorizontalOverflow('chat');
    assert((await page.locator('#chatContextLabel').textContent()).includes('Cow'),'chat identifies the current topic');
    assert.equal(await page.locator('#chatHeading').evaluate(el=>{el.focus({preventScroll:true});return getComputedStyle(el).outlineStyle}),'none','chat heading has no focus outline');
    await page.locator('#chatInput').fill('A draft question');
    await activate(page.locator('#closeChat'));await activate(page.locator('#openChat'));
    assert.equal(await page.locator('#chatInput').inputValue(),'A draft question','closing chat retains an unsent draft');
    const panel=await page.locator('#chatPanel').boundingBox();
    for(const selector of ['#chatInput','.chat-send','#closeChat']){
     const box=await page.locator(selector).boundingBox();
     assert(box&&box.x>=panel.x-1&&box.y>=panel.y-1&&box.x+box.width<=panel.x+panel.width+1&&box.y+box.height<=panel.y+panel.height+1,`${selector} must fit inside the chat panel: ${JSON.stringify({box,panel})}`);
    }
    assert((await page.locator('.chat-log').boundingBox()).height>=64,'conversation area remains readable');
    if(size.mobile){
     for(const selector of ['#chatInput','.chat-send','#closeChat','#clearChat']){
      const box=await page.locator(selector).boundingBox();
      assert(box.height>=44&&box.width>=44,`${selector} should have a comfortable touch target: ${JSON.stringify(box)}`);
     }
    }
    await page.locator('#chatInput').fill('Explain this topic');await activate(page.locator('.chat-send'));
    await page.locator('.chat-rich strong').waitFor();
    assert(requests[0].messages[0].content.includes('Raja Rao · The Cow of the Barricades'));
    assert(requests[0].messages[0].content.includes('Current note (may be abbreviated):'));
    const metrics=await page.locator('.chat-log').evaluate(log=>{const r=log.querySelector('[data-chat-reply="1"]');return {top:r.getBoundingClientRect().top-log.getBoundingClientRect().top}});
    assert(metrics.top>=-1&&metrics.top<30,JSON.stringify(metrics));
    await page.reload();
    await page.waitForFunction(()=>!document.querySelector('#chatPanel').hidden);
    assert((await page.locator('#chatBody').textContent()).includes('brief explanation'),'refresh restores the open chat and recent conversation');
    await activate(page.locator('#closeChat'));assert(!(await page.locator('#chatPanel').isVisible()));
    assert(await page.locator('#openChat').isVisible());
    await activate(page.locator('#saveBtn'));await activate(page.locator('#mobileSaved'));
    assert((await page.locator('#materialBody').textContent()).includes('The Cow of the Barricades'));
    await page.reload();
    await page.waitForFunction(()=>document.querySelector('#readingTitle').textContent==='Saved materials');
    assert((await page.locator('#materialBody').textContent()).includes('The Cow of the Barricades'),'refresh retains the Saved screen');
    assert.equal(await page.locator('#readingTitle').evaluate(el=>{el.focus({preventScroll:true});return getComputedStyle(el).outlineStyle}),'none','saved heading has no focus outline after refresh');
    await activate(page.locator('[data-saved]').first());assert(await page.locator('#openChat').isVisible());
    await activate(page.locator('#backToTopics'));assert(await page.locator('#topicsView').isVisible());
    await activate(page.locator('#preparedPicker [data-topic]').nth(1));await activate(page.locator('#openChat'));
    await page.locator('#chatInput').fill('And this one?');await activate(page.locator('.chat-send'));
    await page.waitForFunction(()=>document.querySelectorAll('.chat-rich').length>=2);
    assert(requests[1].messages[0].content.includes('Aldous Huxley · The Beauty Industry'),'topic context updates');
    assert(requests[1].messages.some(m=>m.content==='Explain this topic'),'unit chat retains memory');
    page.once('dialog',dialog=>dialog.accept());await activate(page.locator('#clearChat'));
    assert.equal(await page.locator('.chat-rich').count(),0,'clear chat removes visible history');
    assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('ammu-chat-history-v1'))['course-19:1']),undefined,'clear chat removes saved history');
    await activate(page.locator('#closeChat'));await page.goBack();assert(await page.locator('#topicsView').isVisible());
    await page.keyboard.press('Tab');await page.locator('#backToHome').focus();
    assert.notEqual(await page.locator('#backToHome').evaluate(el=>getComputedStyle(el).outlineStyle),'none','keyboard focus remains visible on controls');
    await activate(page.locator('#brandHome'));assert(await page.locator('#homeView').isVisible(),'top Ammu name returns home from topics');
    assert((await page.locator('#courseChoice').textContent()).includes('Functional English Ii'),'returning home retains the selected subject');
    await activate(page.locator('#openTopics'));await activate(page.locator('#preparedPicker [data-topic]').first());
    await activate(page.locator('#openChat'));await page.locator('#chatInput').fill('Keep this draft');await activate(page.locator('#closeChat'));
    await activate(page.locator('#brandHome'));assert(await page.locator('#homeView').isVisible(),'top Ammu name returns home from reading');
    await activate(page.locator('#openTopics'));await activate(page.locator('#preparedPicker [data-topic]').first());await activate(page.locator('#openChat'));
    assert.equal(await page.locator('#chatInput').inputValue(),'Keep this draft','returning home retains the unsent chat draft');
    await activate(page.locator('#closeChat'));await activate(page.locator('#mobileSaved'));await activate(page.locator('#brandHome'));
    assert(await page.locator('#homeView').isVisible(),'top Ammu name returns home from saved materials');
    if(!size.mobile){await activate(page.locator('#openTopics'));await activate(page.locator('#sidebarHome'));assert(await page.locator('#homeView').isVisible(),'desktop sidebar Ammu name returns home');}
    assert.deepStrictEqual(errors,[]);console.log('PASS',size.name,`${size.width}x${size.height}`,'navigation, reading, saved, chat and viewport');
   }catch(error){
    fs.mkdirSync('test-results',{recursive:true});const path=`test-results/${size.name}.png`;
    await page.screenshot({path,fullPage:true}).catch(()=>{});console.error('Failure screenshot:',path);throw error;
   }finally{await context.close()}
  }
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
