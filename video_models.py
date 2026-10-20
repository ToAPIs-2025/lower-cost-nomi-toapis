"""Independent T2V comparison. Explicit inspected presets; no POST retry."""
from pathlib import Path
from decimal import Decimal
from urllib.parse import quote
import argparse,hashlib,json,os,time
from media_engine import MediaEngine,save
from toapis_tools.toapis_billing import current_price,observe,cost_summary

PRESETS={
 'MiniMax-H3':{'duration':5,'resolution':'768p','aspect_ratio':'16:9'},
 'kling-3.0-turbo':{'duration':4,'resolution':'720p','aspect_ratio':'16:9','watermark':False},
 'seedance-2-5':{'duration':4,'resolution':'480p','aspect_ratio':'16:9','generate_audio':False,'output_format':'mp4'},
}
def run(model,prompt,engine,live=False):
 if model not in PRESETS or not prompt.strip():raise ValueError('Use an inspected model and nonempty prompt')
 params=PRESETS[model];conditions=dict(params)
 if model=='MiniMax-H3':conditions.update(input_image_count=0,input_video_duration_seconds=0)
 elif model.startswith('kling'):conditions.update(has_image_input=False)
 else:conditions.update(duration='-1',has_image_input=False,has_video_input=False,has_audio_input=False,input_image_count=0)
 rate=current_price(engine.client._json,model,'video',conditions)
 if rate['unit']=='second' and rate['price_basis']=='output_seconds':estimate=Decimal(rate['maximum_unit_price'])*params['duration']
 elif rate['unit']=='1m_tokens' and rate['price_basis']=='total_tokens':estimate=Decimal(rate['maximum_unit_price'])*Decimal(38400)/1000000
 else:raise ValueError('Unsupported price basis')
 if estimate>Decimal('1.50'):raise ValueError('Estimate exceeds per-case cap')
 request={'model':model,'prompt':prompt,**params};identity=hashlib.sha256(json.dumps(request,sort_keys=True).encode()).hexdigest();p=engine.state/(identity+'.json')
 print(json.dumps({'model':model,'estimated_usd':str(estimate),'live':live}),flush=True)
 if not live:return
 if p.exists():
  r=json.loads(p.read_text(encoding='utf-8'))
  if not r['receipt'].get('task_id'):raise RuntimeError('Uncertain earlier submission; no POST retry')
 else:
  r={'kind':'video','status':'submitting','model':model,'parameters':params,'quote':rate,'receipt':{'model':model,'task_id':None,'request':request,'observations':[]}}
  with p.open('x',encoding='utf-8') as f:json.dump(r,f,ensure_ascii=False,indent=2)
  try:data=engine.client._json('videos/generations',request)
  except Exception as e:r.update(status='submission_uncertain',error_type=type(e).__name__,error_message=str(e)[:150]);save(p,r);raise
  r['receipt']['task_id']=data.get('id');observe(r['receipt'],data);r['status']=data.get('status');save(p,r)
  if not r['receipt']['task_id']:raise RuntimeError('Missing task ID; no POST retry')
 deadline=time.monotonic()+1200
 while time.monotonic()<deadline:
  try:data=engine.client._json('videos/generations/'+quote(r['receipt']['task_id'],safe=''))
  except Exception:time.sleep(8);continue
  observe(r['receipt'],data);r['status']=data.get('status');r['cost']=cost_summary(r['receipt']);save(p,r)
  if r['status']=='completed':
   if not r.get('output'):
    raw=engine.client._asset(data['result']['data'][0]['url']);assert b'ftyp' in raw[:40];dest=engine.state/(model+'.mp4');dest.write_bytes(raw);r['output']=str(dest.resolve());save(p,r)
   print(json.dumps({'model':model,'status':r['status'],'cost':r['cost']},ensure_ascii=True),flush=True);return r
  if r['status'] in ('failed','cancelled','expired'):print(json.dumps({'model':model,'status':r['status'],'cost':r['cost']}),flush=True);return r
  time.sleep(8)
 raise RuntimeError('Polling timed out; resume original task only')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--model',choices=list(PRESETS),required=True);p.add_argument('--prompt-file',type=Path,required=True);p.add_argument('--live',action='store_true');a=p.parse_args();run(a.model,a.prompt_file.read_text(encoding='utf-8'),MediaEngine(state=os.environ.get('TOAPIS_STATE_DIR','.toapis-extra-video')),a.live)
