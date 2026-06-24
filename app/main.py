from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="Rouse Local")

app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "Rouse alive"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "Rouse alive"
    }