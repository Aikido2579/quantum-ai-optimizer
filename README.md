    # quantum-ai-optimizer (Upgraded Release)

This release contains:
- Backend (backend/) packaged as quantum_ai_optimizer with CLI `quantum-ai`.
- Frontend (frontend/) React + Vite + Tailwind + Plotly dashboard.
- Docker-compose for dev, GitHub Actions CI workflow, and deploy script.

## Quickstart (backend)
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# install package editable
pip install -e .
# run server
quantum-ai serve --host 0.0.0.0 --port 8000

## Quickstart (frontend)
cd frontend
npm install
npm run dev -- --host

## Or using docker-compose
docker-compose up --build

## Deploy to GitHub
./deploy_to_github.sh git@github.com:YOUR_USERNAME/quantum-ai-optimizer.git
