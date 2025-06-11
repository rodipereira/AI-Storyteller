import streamlit as st
import google.generativeai as genai

# --- Sua chave de API adicionada aqui ---
genai.configure(api_key="YOUR_KEY_API")
# -------------------------------------

st.set_page_config(layout="wide")
st.title("📚 Criador de Histórias Interativas com IA")

st.markdown(
    """
    Crie o início da sua própria aventura! Preencha os campos abaixo para moldar a sua história.
    """
)

# 1. Nome do Protagonista
nome_protagonista = st.text_input("Qual o nome do seu protagonista?", "Ares")

# 2. Gênero Literário
genero = st.selectbox(
    "Escolha o gênero da história:",
    ("Fantasia", "Ficção Científica", "Mistério", "Aventura", "Terror", "Romance")
)

# 3. Local Inicial
local_inicial = st.radio(
    "Onde a história começa?",
    ("Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva", "Um laboratório secreto", "Uma ilha deserta")
)

# 4. Frase de Efeito ou Desafio Inicial
frase_desafio = st.text_area(
    "Adicione uma frase de efeito ou desafio inicial que deve ser incorporada à história:",
    "E de repente, tudo ficou escuro."
)

# Botão para gerar a história
if st.button("Gerar Início da História"):
    if nome_protagonista and genero and local_inicial and frase_desafio:
        # Lógica do Aluno: Criação do prompt para a IA Gemini
        prompt_para_ia = (
            f"Crie o início de uma história de '{genero}' com o protagonista chamado '{nome_protagonista}'. "
            f"A história começa em '{local_inicial}'. "
            f"Incorpore a seguinte frase ou desafio no início: '{frase_desafio}'. "
            "Gere um ou dois parágrafos."
        )

        st.subheader("Seu Prompt para a IA:")
        st.code(prompt_para_ia, language="text")

        # --- Bloco de geração da história com a API Gemini ---
        try:
            # Tente 'gemini-1.0-pro' primeiro
            model = genai.GenerativeModel('gemini-2.0-flash') # <--- MUDANÇA AQUI
            response = model.generate_content(prompt_para_ia)
            historia_gerada = response.text
            st.subheader("Início da Sua História:")
            st.write(historia_gerada)
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar a história: {e}")
            st.info("Certifique-se de que sua API Key do Gemini está configurada corretamente e que você tem acesso à API.")
            st.info("Tente verificar os modelos disponíveis usando `genai.list_models()` ou altere o nome do modelo para 'gemini-1.0-pro'.")
        # -----------------------------------------------------

    else:
        st.warning("Por favor, preencha todos os campos para gerar a história.")

st.markdown("---")
st.markdown("Desenvolvido para o Exercício IA 1 - Criador de Histórias Interativas")
