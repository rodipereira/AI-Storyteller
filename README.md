# 📚 Criador de Histórias Interativas com IA

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-1.x-red.svg" alt="Streamlit Version">
  <img src="https://img.shields.io/badge/Google_Gemini_API-Flash-orange.svg" alt="Google Gemini API">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

## ✨ Visão Geral

Crie o início de histórias interativas usando IA! Este aplicativo Streamlit permite que você defina o protagonista, gênero, local e um desafio inicial, e a IA Gemini gera uma introdução única para sua narrativa. Ideal para explorar **Prompt Engineering** e a criatividade com IA.

## 🚀 Funcionalidades Chave

* **Customização:** Nome do protagonista, gênero (Fantasia, Ficção Científica, Mistério, Aventura, etc.), local (floresta, cidade futurista, castelo, etc.) e frase/desafio inicial.
* **Geração IA:** Um botão para gerar o início da história (1-2 parágrafos) via Google Gemini API.

## 🛠️ Tecnologias

* **Python**
* **Streamlit**
* **Google Gemini API (`gemini-2.0-flash`)**

## 💻 Como Rodar

1.  **Crie a Pasta:** Crie uma pasta para o projeto e coloque `app_historia.py` e `README.md` dentro dela.
2.  **Ambiente Virtual (Opcional):**
    ```bash
    python -m venv venv
    # Windows: .\venv\Scripts\activate
    # Linux/macOS: source venv/bin/activate
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install streamlit google-generativeai
    ```
4.  **Chave de API:** Sua chave de API do Google AI Studio deve estar configurada em `app_historia.py` na linha `genai.configure(api_key="SUACHAVEAPI")`. Substitua `"SUACHAVEAPI"` pela sua chave real (`AIzaSyBlguT0AjfRxC3J-TdBnWEzmoUuQxm5wkg`).
5.  **Execute:**
    ```bash
    streamlit run app_historia.py
    ```

## 💡 Prompt Engineering

O prompt para a IA é construído dinamicamente com base nas suas escolhas, garantindo que a história gerada seja personalizada:

```python
# Exemplo de construção do prompt
prompt_para_ia = (
    f"Crie o início de uma história de '{genero}' com o protagonista chamado '{nome_protagonista}'. "
    f"A história começa em '{local_inicial}'. "
    f"Incorpore a seguinte frase ou desafio no início: '{frase_desafio}'. "
    "Gere um ou dois parágrafos."
)