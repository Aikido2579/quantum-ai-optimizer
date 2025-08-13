@echo off
start cmd /k "cd backend && venv\Scripts\activate && quantum-ai serve"
start cmd /k "cd frontend && npm run dev"
