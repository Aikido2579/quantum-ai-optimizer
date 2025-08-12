@echo off
title Quantum-AI Optimizer Launcher
echo ================================
echo  Starting Quantum-AI Optimizer
echo ================================

REM STEP 1: Start Backend
echo [1/3] Starting Backend...
start cmd /k "cd backend && venv\Scripts\activate && python -m quantum_ai_optimizer"

REM Give backend time to start
timeout /t 5 >nul

REM STEP 2: Start Frontend
echo [2/3] Starting Frontend...
start cmd /k "cd frontend && npm run dev"

REM STEP 3: Wait and open browser
echo [3/3] Opening browser...
timeout /t 5 >nul
start http://localhost:3001

echo ✅ All services started.
pause
