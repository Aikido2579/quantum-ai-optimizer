import click
from .pipeline import pipeline_run, preprocess_run, baseline_run, hybrid_run, evaluate_run
from .app import start_uvicorn

@click.group()
def main():
    """Quantum-AI Optimizer CLI"""
    pass

@main.command('preprocess')
def preprocess_cmd():
    """Run preprocessing"""
    preprocess_run()

@main.command('baseline')
def baseline_cmd():
    """Run baseline training"""
    baseline_run()

@main.command('hybrid')
def hybrid_cmd():
    """Run hybrid quantum training"""
    hybrid_run()

@main.command('evaluate')
def evaluate_cmd():
    """Run evaluation"""
    evaluate_run()

@main.command('run-pipeline')
def run_pipeline_cmd():
    """Run full pipeline"""
    pipeline_run()

@main.command('serve')
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=8000)
def serve_cmd(host, port):
    """Start backend server (uvicorn)"""
    start_uvicorn(host=host, port=port)

if __name__ == '__main__':
    main()
