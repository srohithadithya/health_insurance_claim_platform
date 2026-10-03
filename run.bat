@echo off
REM run.bat - Windows launcher using uv

cd /d "%~dp0"

echo Creating virtual environment with uv...
uv venv --python 3.11

echo Activating venv and installing dependencies...
call .venv\Scripts\activate
uv pip install -r requirements.txt

echo Starting FastAPI server...
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
pause