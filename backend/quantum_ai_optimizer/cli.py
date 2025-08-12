import click
from quantum_ai_optimizer.datasets.eeg_loader import load_sample_eeg, preprocess_eeg

@click.group()
def cli():
    """Quantum-AI Optimizer CLI"""
    pass

@cli.command()
def baseline():
    """Run baseline training"""
    print("[Baseline] Training baseline model...")

@cli.command()
def evaluate():
    """Run evaluation"""
    print("[Evaluate] Running evaluation...")

@cli.command()
def hybrid():
    """Run hybrid quantum training"""
    print("[Hybrid] Running quantum-classical model...")

@cli.command()
def preprocess():
    """Run preprocessing"""
    print("[Preprocess] Running preprocessing pipeline...")

@cli.command()
def run_pipeline():
    """Run full pipeline"""
    print("[Pipeline] Running full pipeline...")

@cli.command()
def serve():
    """Start backend server (uvicorn)"""
    import uvicorn
    uvicorn.run("quantum_ai_optimizer.app:app", host="0.0.0.0", port=8000, reload=True)

@cli.command()
def eeg():
    """Run EEG data load + preprocessing"""
    raw = load_sample_eeg()
    raw_filtered = preprocess_eeg(raw)
    print("[EEG Pipeline] Ready to pass filtered EEG data to model.")

if __name__ == "__main__":
    cli()
