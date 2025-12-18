from fastapi import FastAPI

app = FastAPI(title="SentinelStream Fraud Detection API")

@app.get("/")
def root():
    return {"message": "SentinelStream API is running"}
