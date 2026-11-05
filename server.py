import os,json,urllib.request,urllib.error
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,format,*args): pass
 def respond(self,status,obj):
  data=json.dumps(obj).encode(); self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(data))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(data)
 def do_GET(self):
  if self.path=='/api/status': return self.respond(200,{'configured':bool(os.getenv('AI_API_KEY') and os.getenv('AI_MODEL')),'model':os.getenv('AI_MODEL','')})
  if self.path.startswith('/api/'): return self.respond(404,{'error':'Not found'})
  return super().do_GET()
 def do_POST(self):
  if self.path!='/api/chat': return self.respond(404,{'error':'Not found'})
  key=os.getenv('AI_API_KEY',''); model=os.getenv('AI_MODEL',''); base=os.getenv('AI_BASE_URL','https://api.openai.com/v1').rstrip('/')
  if not key or not model: return self.respond(503,{'error':'AI is not connected yet. Set AI_API_KEY, AI_MODEL and AI_BASE_URL on the server, then restart it.'})
  if not base.startswith('https://'): return self.respond(400,{'error':'AI_BASE_URL must use HTTPS.'})
  try:
   length=int(self.headers.get('Content-Length','0'))
   if length>60000: return self.respond(413,{'error':'Request too large.'})
   data=json.loads(self.rfile.read(length)); messages=data.get('messages',[])
   if not isinstance(messages,list) or not messages or len(messages)>30: raise ValueError('Invalid messages')
   clean=[{'role':m['role'],'content':str(m['content'])[:12000]} for m in messages if isinstance(m,dict) and m.get('role') in ('system','user','assistant') and 'content' in m]
   req=urllib.request.Request(base+'/chat/completions',data=json.dumps({'model':model,'messages':clean,'temperature':0.5}).encode(),headers={'Content-Type':'application/json','Authorization':'Bearer '+key},method='POST')
   with urllib.request.urlopen(req,timeout=100) as res: result=json.load(res)
   text=result['choices'][0]['message']['content']; self.respond(200,{'text':text})
  except urllib.error.HTTPError as e:
   self.respond(502,{'error':f'AI provider returned HTTP {e.code}. Check the model, API key, quota and base URL.'})
  except Exception as e: self.respond(502,{'error':'Could not reach the AI provider. Check your configuration and connection.'})
if __name__=='__main__':
 ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT','8000'))),Handler).serve_forever()
