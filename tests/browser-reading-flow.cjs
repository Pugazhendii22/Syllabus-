// Optional browser integration test: run server.py and install Playwright Chromium first. AI responses are mocked.
const {chromium}=require('playwright');
const assert=require('assert');
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 for(const size of [{width:390,height:844},{width:1440,height:900}]){
  const context=await browser.newContext({viewport:size,deviceScaleFactor:1,serviceWorkers:'block'}), page=await context.newPage();
  let errors=[];page.on('pageerror',e=>errors.push(e.message));let requests=[];
  await page.route('**/api/chat',async route=>{requests.push(route.request().postDataJSON());await route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({text:'### Answer\n\nA **brief explanation**.\n\n'+('A longer explanation for reading. '.repeat(120))})})});
  await page.goto('http://127.0.0.1:8000/');await page.locator('#courseChoice').waitFor();
  await page.waitForFunction(()=>document.querySelector('#courseChoice').textContent.includes('English Literature'));
  assert(await page.locator('#homeView').isVisible());assert(!(await page.locator('#topicsView').isVisible()));
  await page.locator('#semTabs [data-sem="3"]').click();await page.locator('#courseChoice').click();
  await page.locator('#choiceList button').filter({hasText:'Functional English Ii'}).click();
  await page.locator('#unitChoice').click();await page.locator('#choiceList button').nth(1).click();
  assert(await page.locator('#topicsView').isVisible());assert(!(await page.locator('#homeView').isVisible()));
  assert.equal(await page.locator('#preparedPicker [data-topic]').count(),3);
  await page.locator('#preparedPicker [data-topic]').first().click();
  assert(await page.locator('#readingView').isVisible());assert(!(await page.locator('#topicsView').isVisible()));
  assert((await page.locator('#readingTitle').textContent()).includes('Cow'));
  assert(await page.locator('#openChat').isVisible());
  const fab=await page.locator('#openChat').boundingBox();assert(fab.y>=0&&fab.y+fab.height<=size.height,'floating assistant stays within viewport');
  const before=await page.locator('#materialBody').textContent();await page.locator('#openChat').click();
  assert.equal(await page.locator('#materialBody').textContent(),before);
  await page.locator('#chatInput').fill('Explain this topic');await page.locator('.chat-send').click();
  await page.locator('.chat-rich strong').waitFor();
  assert(requests[0].messages[0].content.includes('Raja Rao · The Cow of the Barricades'));
  assert(requests[0].messages[0].content.includes('Current note (may be abbreviated):'));
  const metrics=await page.locator('.chat-log').evaluate(log=>{const r=log.querySelector('[data-chat-reply="1"]');return {top:r.getBoundingClientRect().top-log.getBoundingClientRect().top, scrollTop:log.scrollTop, scrollHeight:log.scrollHeight,clientHeight:log.clientHeight}});
  assert(metrics.top>=-1&&metrics.top<30,JSON.stringify(metrics));
  const overflow=await page.evaluate(()=>({doc:document.documentElement.scrollWidth,view:window.innerWidth}));assert(overflow.doc<=overflow.view,JSON.stringify(overflow));
  await page.locator('#closeChat').click();assert(!(await page.locator('#chatPanel').isVisible()));
  await page.locator('#saveBtn').click();await page.locator('#mobileSaved').click();assert((await page.locator('#materialBody').textContent()).includes('The Cow of the Barricades'));
  await page.locator('[data-saved]').first().click();assert(await page.locator('#openChat').isVisible());
  await page.locator('#backToTopics').click();assert(await page.locator('#topicsView').isVisible());
  await page.locator('#preparedPicker [data-topic]').nth(1).click();await page.locator('#openChat').click();await page.locator('#chatInput').fill('And this one?');await page.locator('.chat-send').click();await page.waitForFunction(()=>document.querySelectorAll('.chat-rich').length>=2);
  assert(requests[1].messages[0].content.includes('Aldous Huxley · The Beauty Industry'),'topic context updates after changing topic');
  assert(requests[1].messages.some(m=>m.content==='Explain this topic'),'unit chat retains memory');
  page.once('dialog',dialog=>dialog.accept());await page.locator('#clearChat').click();
  assert.equal(await page.locator('.chat-rich').count(),0,'clear chat removes visible history');
  assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('ammu-chat-history-v1'))['course-19:1']),undefined,'clear chat removes saved history');
  await page.locator('#closeChat').click();await page.goBack();assert(await page.locator('#topicsView').isVisible());
  assert.deepStrictEqual(errors,[]); console.log('PASS browser',size.width,'navigation, reading, saved, topic-aware mocked AI, memory and scroll');
  await context.close();
 }
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
