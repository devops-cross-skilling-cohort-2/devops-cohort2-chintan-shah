# FastAPI Health API

Small FastAPI app exposing a GET /health endpoint that returns JSON {"status": "ok"}.

Requirements are in `requirements.txt`.

Run locally (macOS, zsh):

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Validate locally:
```bash
curl http://127.0.0.1:8000/health
```
This should print the response `{"status":"ok","version":"1.0.0","environment":"dev","timestamp":"2026-05-27T10:28:25.126339"}` (timestamp will be a dynamic value indicating current approximate timestamp)

Run tests:

```bash
pytest -q
```
