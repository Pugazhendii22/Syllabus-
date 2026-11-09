// Launch an isolated preview server for browser tests and stop it afterwards.
const {spawn}=require('child_process');
const net=require('net');
(async()=>{
 const probe=net.createServer();
 await new Promise((resolve,reject)=>probe.once('error',reject).listen(0,'127.0.0.1',resolve));
 const port=probe.address().port;
 await new Promise(resolve=>probe.close(resolve));
 const base=`http://127.0.0.1:${port}`;
 const server=spawn(process.env.PYTHON||'python3',['server.py'],{env:{...process.env,PORT:String(port)},stdio:['ignore','ignore','pipe']});
 let serverError='';server.stderr.on('data',chunk=>serverError+=chunk);
 try{
  let ready=false;
  for(let i=0;i<100;i++){
   if(server.exitCode!==null)throw Error(`Preview server exited: ${serverError}`);
   try{const response=await fetch(base);if(response.ok){ready=true;break}}catch{}
   await new Promise(resolve=>setTimeout(resolve,100));
  }
  if(!ready)throw Error('Preview server did not start: '+serverError);
  for(const testFile of ['tests/browser-reading-flow.cjs','tests/swipe-chat.cjs','tests/spoken-downloads.cjs']){
   const test=spawn(process.execPath,[testFile],{stdio:'inherit',env:{...process.env,AMMU_TEST_URL:base}});
   const result=await new Promise((resolve,reject)=>{test.once('error',reject);test.once('exit',(code,signal)=>resolve({code,signal}))});
   if(result.code!==0)throw Error(`Mobile UI tests failed (${testFile}: ${result.signal||result.code})`);
  }
 }finally{server.kill('SIGTERM')}
})().catch(error=>{console.error(error);process.exitCode=1});
