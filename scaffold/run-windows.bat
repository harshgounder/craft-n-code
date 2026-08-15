@echo off
rem Craft N Code 2026 shared scaffold - one-command launcher (Windows)
rem Same behavior as demo.sh: generate the feed, then serve.
rem Usage: run-windows.bat [--port PORT] [--auth TOKEN]
setlocal
set "PORT=8137"
set "AUTH="

:parse
if "%~1"=="" goto serve
if /i "%~1"=="--port" (
  set "PORT=%~2"
  shift
  shift
  goto parse
)
if /i "%~1"=="--auth" (
  set "AUTH=%~2"
  shift
  shift
  goto parse
)
if /i "%~1"=="--help" (
  echo Usage: run-windows.bat [--port PORT] [--auth TOKEN]
  exit /b 0
)
echo unknown arg: %~1
exit /b 1

:serve
if not defined PORT set "PORT=8137"
if not defined OLLAMA_API_KEY (
  echo [run] no OLLAMA_API_KEY -^> offline mode (rule-based, zero network)
) else (
  echo [run] using ollama-cloud LLM
)
python engine\engine.py --seed --out webapp\static\demo-feed.json
if errorlevel 1 exit /b %errorlevel%

set "ARGS=--port %PORT%"
if defined AUTH set "ARGS=%ARGS% --auth %AUTH%"
echo [run] open http://localhost:%PORT%
python webapp\serve.py %ARGS%
endlocal
exit /b %errorlevel%
