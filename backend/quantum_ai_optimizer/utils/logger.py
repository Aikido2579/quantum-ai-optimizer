import os
import json

def create_run_folder(run_name, overwrite=False):
    """
    Creates a folder in results/ for storing run artifacts.
    If overwrite=True, existing files are cleared.
    """
    path = os.path.join("results", run_name)
    if overwrite and os.path.exists(path):
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
    os.makedirs(path, exist_ok=True)
    return path

def save_metrics(run_path, metrics):
    """
    Save metrics dictionary as JSON inside run_path.
    """
    with open(os.path.join(run_path, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
