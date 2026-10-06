from client.client import OllamaClient
from schemas.sentimentSchema import ClientRequest, SentimentResponse


async def analyze_sentiment(
    request: ClientRequest,
) -> SentimentResponse:

    prompt = f"""
You are a customer sentiment analysis AI.

Analyze the following customer message carefully.

Customer Message:
{request.text}

Determine:

1. Overall sentiment:
   - positive
   - negative
   - neutral
   - mixed

2. Confidence:
   - A value between 0 and 1.

3. Primary emotion:
   - happy
   - satisfied
   - frustrated
   - angry
   - sad
   - disappointed
   - confused
   - neutral

4. Urgency:
   - low
   - medium
   - high
   - critical

5. Main topics discussed.

6. A short summary of the customer's message.

7. A recommended action for the customer support team.

Rules:
- Analyze only the information provided by the customer.
- Do not invent facts.
- Be objective.
- Return the result according to the provided response schema.
"""

    result = await OllamaClient.analyze_sentiment(prompt=prompt)
    result = SentimentResponse.model_validate_json(result)
    result.customer_id = request.customer_id

    return result
