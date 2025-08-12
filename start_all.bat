@echo off
REM Activate backend venv and start backend in a new terminal
start cmd /k "cd backend && venv\Scripts\activate && python -m quantum_ai_optimizer.cli serve"

REM Start frontend
cd frontend
npm run dev
