# 💰 BIA - Assistente Financeiro Inteligente

> Um assistente virtual financeiro que utiliza Inteligência Artificial (Google Gemini) para responder dúvidas personalizadas com base no perfil e histórico do usuário.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio prático (Lab) da **DIO**. O objetivo é criar um agente financeiro que não apenas responde perguntas genéricas, mas utiliza **RAG (Retrieval-Augmented Generation)** para analisar dados fictícios de um cliente (transações, perfil de investidor e produtos bancários) e fornecer consultoria personalizada.

### ✨ Funcionalidades
* **Consulta de Saldo e Gastos:** Analisa um arquivo CSV de transações para responder sobre o histórico financeiro.
* **Recomendação de Investimentos:** Cruza o perfil do investidor com produtos financeiros disponíveis (JSON).
* **Respostas Naturais:** Utiliza a API do Google Gemini Pro para gerar respostas fluidas e amigáveis.
* **Interface Web:** Chatbot simples e responsivo feito com HTML/CSS/JS.

---

## 🚀 Tecnologias Utilizadas

* **Backend:** Python, FastAPI, Uvicorn
* **IA:** Google Gemini API (`google-generativeai`)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Dados:** JSON e CSV (Mockados)

---

## 📦 Como Rodar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.
* Uma chave de API do Google Gemini (Google AI Studio).
