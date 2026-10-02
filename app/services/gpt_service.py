from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv() #contains api

client = AsyncOpenAI()

async def generate_response(messages: list):
    response = await client.responses.create(
        model="gpt-5.4-mini",
        input= messages
    )
    return response.output_text
