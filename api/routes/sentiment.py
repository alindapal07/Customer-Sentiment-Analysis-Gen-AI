from fastapi import APIRouter

from schemas.sentimentSchema import ClientRequest, SentimentResponse
from services.sentiment_services import analyze_sentiment

router = APIRouter(
    prefix="/api/v1/sentiment",
    tags=["Sentiment"],
)


@router.post(
    "/analyze",
    response_model=SentimentResponse,
)
async def analyze(request: ClientRequest):
    return await analyze_sentiment(request)
