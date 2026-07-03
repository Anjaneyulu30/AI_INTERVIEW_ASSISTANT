from fastapi import FastAPI

app = FastAPI(
    title="AI Interview Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Interview Assistant API is running"
    }