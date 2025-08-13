from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for live updates"""
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except:
        connected_clients.remove(websocket)

async def send_ws_message(msg: dict):
    """Send JSON message to all connected WebSocket clients"""
    for ws in connected_clients:
        try:
            await ws.send_json(msg)
        except:
            pass

@app.post("/run/pipeline")
async def run_pipeline_endpoint():
    """HTTP endpoint to run pipeline with WS updates"""
    from quantum_ai_optimizer.pipeline.preprocess import preprocess_run as preprocess_all
    from quantum_ai_optimizer.pipeline.baseline import baseline_run as train_baseline
    from quantum_ai_optimizer.pipeline.hybrid import hybrid_run as train_hybrid

    await send_ws_message({"status": "Starting pipeline..."})
    preprocess_all()
    await send_ws_message({"status": "Preprocessing done"})
    train_baseline()
    await send_ws_message({"status": "Baseline training done"})
    train_hybrid()
    await send_ws_message({"status": "Hybrid training done"})
    await send_ws_message({"status": "✅ Pipeline complete"})

    return {"message": "Pipeline finished"}
