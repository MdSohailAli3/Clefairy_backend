from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.gpt_service import generate_response
from app.services.memory_service import (
    get_or_create_conversation,
    add_user_message,
    add_assistant_message,
    format_for_llm_from_doc
)

router = APIRouter(prefix="/users",tags=["Chat-Bot"])

# route - >  /users/chat/id
@router.post("/chat/{user_id}")
async def chat(user_id: int, request: ChatRequest):

    # Ensure conversation exists, ignore returned
    await get_or_create_conversation(user_id)

    # Store user message
    conversation = await add_user_message(user_id, request.message)

    if conversation is None:
        raise RuntimeError("Conversation should not be None")
    
    # Prepare messages for LLM
    formatted_messages = await format_for_llm_from_doc(conversation)

    # Generate response
    response = await generate_response(formatted_messages)

    # Store assistant reply
    await add_assistant_message(user_id, response)

    return {"response": response}

