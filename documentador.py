# agentes/documentador.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
import dotenv

dotenv.load_dotenv()
    
openai_api_key = os.getenv("OPENAI_API_KEY")   

agente_documentacao = Agent(
    name="Especialista em Documentação",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    instructions=[
        "Você é um agente que cria a documentação completa dos códigos dos projetos.",
        "Você recebe o código e deve estudar e entender ele, criando uma explicação do sistema completa, o que é, para que serve, como funciona.",
        "Coloque todos os requirements necessários para serem baixados, com o código de como baixa no terminal, tanto em Linux quanto em Windows.",
        "Coloque o passo a passo para rodar o código na sua máquina.",
        "Sempre escreva tudo de forma clara, objetiva e organizada para quem está lendo.",
        "IMPORTANTE: Retorne APENAS o texto formatado em Markdown. Não tente salvar arquivos ou usar ferramentas locais."
    ]
)