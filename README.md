# FastAPI Health API

Small FastAPI app exposing a GET /health endpoint that returns JSON {"status": "ok"}.

Requirements are in `requirements.txt`.

Run locally (macOS, zsh):

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Run tests:

```bash
pytest -q
```
