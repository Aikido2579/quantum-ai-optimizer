@echo off
echo ==========================
echo  Starting Quantum-AI Optimizer
echo ==========================

REM Step 1: Start Backend
echo.
echo [1/3] Starting Backend...
start cmd /k "cd backend && venv\Scripts\activate && python -m quantum_ai_optimizer"

REM Give backend a moment to start
timeout /t 5 >nul

REM Step 2: Test Backend
echo.
echo [2/3] Testing Backend API...
curl http://127.0.0.1:8000/ || echo Backend not responding. Check logs.

REM Step 3: Start Frontend
echo.
echo [3/3] Starting Frontend...
start cmd /k "cd frontend && npm install && npm run dev"

echo.
echo ✅ Both backend and frontend have been started in separate windows.
pause
