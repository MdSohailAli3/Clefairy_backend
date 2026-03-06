import replicate
from dotenv import load_dotenv
import asyncio

load_dotenv() #contains api

# request and response from api
async def generate_response(messages: list):
    def call_replicate():
        output = replicate.run( # it is synchrounous 
            "openai/gpt-5",
            input={
                "messages": messages,
                "max_output_tokens": 200

            }
        )

        return "".join(output)

    response = await asyncio.to_thread(call_replicate)

    return response
