// Chromium phone emulation, including actual offline download bytes (not a physical-device test).
const {chromium}=require('playwright');
const assert=require('assert');
const fs=require('fs');
const crypto=require('crypto');
const base=process.env.AMMU_TEST_URL || 'http://127.0.0.1:8000';
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 const context=await browser.newContext({viewport:{width:360,height:640},isMobile:true,hasTouch:true,acceptDownloads:true});
 const page=await context.newPage(), errors=[];page.on('pageerror',e=>errors.push(e.message));
 try{
  await page.goto(base);await page.waitForFunction(()=>document.querySelector('#courseChoice').textContent.includes('English Literature'));
  await page.evaluate(()=>navigator.serviceWorker.ready);
  await page.reload();await page.waitForFunction(()=>navigator.serviceWorker.controller && document.querySelector('#courseChoice').textContent.includes('English Literature'));
  await page.locator('#courseChoice').tap();await page.locator('#choiceList button').filter({hasText:'Spoken English'}).tap();
  await page.locator('#unitChoice').tap();await page.locator('#choiceList button').nth(2).tap();
  assert(await page.locator('#openDownloadsTopics').isVisible());
  await page.locator('#openDownloadsTopics').tap();
  assert.equal(await page.locator('#downloadScope').inputValue(),'3','current unit selected by default');
  assert.equal(await page.locator('#downloadFormat').inputValue(),'pdf');
  assert(await page.locator('#downloadHelp').textContent().then(x=>x.includes('Word is editable')));
  const dims=await page.evaluate(()=>({doc:document.documentElement.scrollWidth,view:innerWidth}));assert(dims.doc<=dims.view,'no horizontal overflow');
  await context.setOffline(true);
  for(const scope of ['all','1','2','3','4','5'])for(const format of ['pdf','docx']){
   // Chromium limits automatic downloads per document; a reload resets that limit.
   if(scope==='4' && format==='pdf'){await page.reload();await page.waitForFunction(()=>!document.querySelector('#topicsView').hidden);await page.locator('#openDownloadsTopics').tap();}
   await page.locator('#downloadScope').selectOption(scope);await page.locator('#downloadFormat').selectOption(format);
   const path=scope==='all'?(format==='pdf'?'notes/spoken-english/Spoken_English_Notes.pdf':'notes/spoken-english/downloads/Spoken-English-All-Units.docx'):`notes/spoken-english/downloads/Spoken-English-Unit-${scope}.${format}`;
   assert.equal(await page.locator('#downloadFile').getAttribute('href'),'/'+path);
   const [download]=await Promise.all([page.waitForEvent('download'),page.locator('#downloadFile').tap()]);
   assert.equal(await download.failure(),null,`${scope} ${format} download`);
   const chunks=[];for await(const chunk of await download.createReadStream())chunks.push(chunk);
   assert.equal(sha(Buffer.concat(chunks)),sha(fs.readFileSync(path)),`${scope} ${format} must contain the actual complete file`);
  }
  await page.locator('#closeDownload').tap();await page.locator('#preparedPicker [data-topic]').filter({hasText:'Original PDF notes'}).tap();
  assert((await page.locator('#materialBody').textContent()).includes('The Honest Woodcutter'),'new detailed PDF transcription appears in Unit III');
  assert(await page.locator('#openDownloadsReading').isVisible(),'downloads also available in the reading screen');
  await page.locator('#openDownloadsReading').tap();assert.equal(await page.locator('#downloadScope').inputValue(),'3');await page.locator('#closeDownload').tap();
  await page.reload();await page.waitForFunction(()=>!document.querySelector('#readingView').hidden);
  assert(await page.locator('#openDownloadsReading').isVisible(),'offline shell remains HTML after downloads');
  assert.equal(errors.length,0,errors.join('\n'));console.log('PASS: all 12 real downloads, offline bytes, unit selection, reading screen and shell (Chromium mobile emulation)');
 }finally{await context.close();await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
