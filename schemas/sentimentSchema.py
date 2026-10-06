from pydantic import BaseModel, Field
from typing import Literal, Optional


class ClientRequest(BaseModel):
    customer_id: str | None = None
    text: str = Field(min_length=1, max_length=5000)


class SentimentResponse(BaseModel):
    customer_id: str | None = None
    sentiment: Literal["positive", "negative", "neutral", "mixed"] = Field(
        description="Overall sentiment expressed by the customer."
    )

    confidence: float = Field(
        ge=0, le=1, description="Confidence score between 0 and 1."
    )

    emotion: Literal[
        "happy",
        "satisfied",
        "frustrated",
        "angry",
        "sad",
        "disappointed",
        "confused",
        "neutral",
    ] = Field(description="Primary emotion expressed by the customer.")

    urgency: Literal["low", "medium", "high", "critical"] = Field(
        description="Urgency of the customer's issue."
    )

    topics: list[str] = Field(
        description="Main topics mentioned in the customer's message."
    )

    summary: str = Field(description="Short summary of the customer's message.")

    recommended_action: str = Field(
        description="Recommended action for the customer support team."
    )
