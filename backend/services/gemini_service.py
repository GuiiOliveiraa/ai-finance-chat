import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def carregar_dados_contexto():
    """
    Carrega os arquivos JSON e CSV da pasta data para usar como contexto.
    Ajusta os caminhos baseados na estrutura de pastas.
    """
    try:
        # Pega o diretório atual (backend/services) e sobe níveis para chegar na raiz
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, "dio-lab-bia-do-futuro", "data")

        # Carregar Perfil
        caminho_perfil = os.path.join(data_dir, "perfil_investidor.json")
        with open(caminho_perfil, "r", encoding="utf-8") as f:
            perfil = f.read()

        # Carregar Produtos
        caminho_produtos = os.path.join(data_dir, "produtos_financeiros.json")
        with open(caminho_produtos, "r", encoding="utf-8") as f:
            produtos = f.read()

        # Carregar Transações (Lendo como texto simples para economizar processamento)
        caminho_transacoes = os.path.join(data_dir, "transacoes.csv")
        with open(caminho_transacoes, "r", encoding="utf-8") as f:
            transacoes = f.read()

        return perfil, produtos, transacoes
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return "{}", "[]", ""

def ask_gemini(message):
    try:
        # 1. Carrega os dados atualizados
        perfil, produtos, transacoes = carregar_dados_contexto()

        # 2. Cria o System Prompt (A "Personalidade" e o "Conhecimento" da BIA)
        system_instruction = f"""
        Você é a BIA, uma assistente financeira pessoal, inteligente e proativa.
        
        CONTEXTO DO CLIENTE (Use isso para personalizar a resposta):
        ---
        PERFIL DO INVESTIDOR:
        {perfil}
        
        HISTÓRICO DE TRANSAÇÕES RECENTES:
        {transacoes}
        ---

        BASE DE CONHECIMENTO (Produtos disponíveis no banco):
        {produtos}
        
        SUAS DIRETRIZES:
        1. Responda de forma curta, amigável e consultiva.
        2. Use os dados acima para dar respostas precisas (ex: se perguntarem o saldo, calcule ou busque nos dados).
        3. Se o usuário perguntar sobre investimentos, recomende produtos que combinem com o "perfil_investidor" dele.
        4. Nunca invente dados que não estejam no contexto.
        5. Se a pergunta não for sobre finanças, diga educadamente que só pode ajudar com esse tema.

        PERGUNTA DO USUÁRIO:
        {message}
        """

        # 3. Envia tudo para o Gemini
        response = model.generate_content(system_instruction)
        return response.text
    except Exception as e:
        return f"Desculpe, tive um erro técnico: {str(e)}"