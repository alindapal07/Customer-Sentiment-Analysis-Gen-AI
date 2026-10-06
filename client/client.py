# from google import genai
# from google.genai import types
from ollama import AsyncClient

from core.config import settings
from schemas.sentimentSchema import SentimentResponse


class OllamaClient:

    def __init__(self):
        self.client = AsyncClient(host=settings.OLLAMA_HOST)

    async def analyze_sentiment(
        self,
        prompt: str,
    ) -> str:
        response = await self.client.chat(
            model=settings.OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            format=SentimentResponse.model_json_schema(),
            options={
                "temperature": 0,
            },
        )

        if not response.message.content:
            raise ValueError("Ollama returned an empty response.")

        return response.message.content


OllamaClient = OllamaClient()
