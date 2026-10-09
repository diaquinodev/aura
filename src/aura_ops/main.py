from fastapi import FastAPI

app = FastAPI(title="Aura Ops")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
