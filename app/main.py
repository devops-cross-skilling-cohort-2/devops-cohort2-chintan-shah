from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    """Health check endpoint returning simple JSON status."""
    return {"status": "ok"}
