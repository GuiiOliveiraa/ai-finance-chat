from fastapi import APIRouter
from services.gemini_service import ask_gemini

router = APIRouter()

@router.post("/chat")
async def chat(data: dict):
    msg = data.get("message")

    if not msg:
        return {"response":"Mensagem vazia"}

    if len(msg) > 300:
        return {"response":"Mensagem muito longa"}

    response = ask_gemini(msg)
    return {"response": response}
