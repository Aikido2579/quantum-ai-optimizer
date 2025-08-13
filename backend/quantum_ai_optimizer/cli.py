import click
import asyncio
from quantum_ai_optimizer.pipeline.preprocess import preprocess_run as preprocess_all
from quantum_ai_optimizer.pipeline.baseline import baseline_run as train_baseline
from quantum_ai_optimizer.pipeline.hybrid import hybrid_run as train_hybrid
from quantum_ai_optimizer.app import send_ws_message


@click.group()
def cli():
    """Quantum-AI Optimizer CLI"""
    pass


@cli.command(name="serve")
def serve_cmd():
    """Start backend API + WebSocket server"""
    import uvicorn
    uvicorn.run(
        "quantum_ai_optimizer.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )


@cli.command(name="run-pipeline")
def run_pipeline_cmd():
    """Run full pipeline: preprocess → baseline → hybrid"""
    loop = asyncio.get_event_loop()

    async def run_steps():
        await send_ws_message({"status": "Starting pipeline..."})
        preprocess_all()
        await send_ws_message({"status": "Preprocessing done"})
        train_baseline()
        await send_ws_message({"status": "Baseline training done"})
        train_hybrid()
        await send_ws_message({"status": "Hybrid training done"})
        await send_ws_message({"status": "✅ Pipeline complete"})

    loop.run_until_complete(run_steps())
