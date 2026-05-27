from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/health")
async def health():
    """Health check endpoint returning simple JSON status."""
    return {"status": "ok", "version": "1.0.0", "environment": "dev", "timestamp": datetime.now()}
