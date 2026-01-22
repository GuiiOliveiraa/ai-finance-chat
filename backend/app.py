from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import router

app = FastAPI()

# Configuração do CORS para permitir que o frontend converse com o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem (para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"status": "API rodando"}