from fastapi import FastAPI
from api.routes.sentiment import router as sentiment_router


app = FastAPI(
    title="Customer Sentiment AI",
    version="1.0.0",
)

app.include_router(sentiment_router)


@app.get("/")
def root():
    return "Hello from fastapi application home page"
