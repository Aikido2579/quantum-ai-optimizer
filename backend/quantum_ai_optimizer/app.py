import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
import json, threading, time
from .datasets.simulator import Simulator
from .pipeline import pipeline_run, preprocess_run, baseline_run, hybrid_run, evaluate_run

app = FastAPI(title='Quantum-AI Optimizer')

sim = Simulator()

@app.get('/health')
def health():
    return JSONResponse({'status':'ok'})

@app.post('/run/pipeline')
def run_pipeline():
    def _run():
        try:
            pipeline_run()
        except Exception as e:
            print('Pipeline error:', e)
    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return JSONResponse({'status':'started'})

@app.get('/ws/demo')
def get_demo():
    html = """<!doctype html><html><body><h1>WebSocket Demo</h1>
    <script>
    const ws = new WebSocket('ws://' + location.host + '/ws/stream');
    ws.onmessage = (ev)=>{ console.log('msg', ev.data); document.body.prepend(document.createElement('pre')).textContent = ev.data; };
    </script></body></html>"""
    return HTMLResponse(html)

@app.websocket('/ws/stream')
async def websocket_stream(ws: WebSocket):
    await ws.accept()
    try:
        for msg in sim.stream_generator():
            await ws.send_text(json.dumps(msg))
            time.sleep(0.5)
    except WebSocketDisconnect:
        print('Client disconnected')

def start_uvicorn(host='0.0.0.0', port=8000):
    uvicorn.run("quantum_ai_optimizer.app:app", host=host, port=port, reload=True)
