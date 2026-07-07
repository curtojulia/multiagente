import streamlit as st
import os
import dotenv
from documentador import agente_documentacao
from performance import agente_performance
from seguranca import agente_seguranca

# Carrega as chaves de API
dotenv.load_dotenv()

# Configuração da página do Streamlit
st.set_page_config(page_title="Verificador de Código IA", page_icon="🤖", layout="wide")

st.title("🤖 Verificador de Código Multiagentes")
st.write("Cole seu código e selecione o que deseja fazer no menu lateral.")

# 1. CRIANDO O MENU LATERAL
st.sidebar.header("Menu de Opções")
opcao = st.sidebar.selectbox(
    "O que você deseja fazer?",
    ["Selecione...", "Gerar README.md", "Analisar Segurança", "Otimizar Performance"]
)

# 2. ÁREA PRINCIPAL DE INPUT
codigo_usuario = st.text_area("Cole o seu código aqui abaixo:", height=300, placeholder="def minha_funcao()...")
codigo_usuario_strip = codigo_usuario.strip()  # Armazena valor stripado

# Função para executar análise
def executar_analise(opcao):
    if not codigo_usuario_strip:
        st.warning("⚠️ Por favor, cole algum código antes de executar.")
        return

    if opcao == "Gerar README.md":
        with st.spinner("🚀 O Especialista em Documentação está estudando seu código..."):
            resposta = agente_documentacao.run(f"Por favor, estude e documente este código:\n{codigo_usuario}")
            st.success("✨ Documentação gerada com sucesso!")
            st.markdown(resposta.content)
            st.download_button(
                label="📥 Baixar arquivo README.md",
                data=resposta.content,
                file_name="README.md",
                mime="text/markdown"
            )

    elif opcao == "Otimizar Performance":
        with st.spinner("📈 O Engenheiro de Performance está calculando os gargalos..."):
            resposta = agente_performance.run(f"Por favor, analise e otimize este código:\n{codigo_usuario}")
            st.success("🏁 Análise de Performance concluída!")
            st.markdown(resposta.content)

    elif opcao == "Analisar Segurança":
        with st.spinner("🔍 O Especialista em Segurança está examinando seu código..."):
            resposta = agente_seguranca.run(f"Por favor, analise este código quanto a vulnerabilidades de segurança:\n{codigo_usuario}")
            st.success("✅ Análise de Segurança concluída!")
            st.markdown(resposta.content)

# 3. PROCESSAMENTO DA OPÇÃO SELECIONADA
if opcao != "Selecione...":
    if st.button("Executar"):
        executar_analise(opcao)