from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
import dotenv
dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

agente_seguranca = Agent(
    name="Especialista em Segurança",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    instructions=[
        "Você atua como um auditor de segurança sênior.",
        "Sua missão é verificar no código recebido se há alguma falha de segurança, dados sensíveis expostos (como senhas ou chaves de API escritas direto no código) ou qualquer outra vulnerabilidade.",
        "Se encontrar problemas, você deve gerar a versão corrigida do código aplicando as correções necessárias.",
        "Recomende boas práticas de segurança aplicadas ao contexto do código analisado.",
        "Sempre explique o motivo de cada correção e recomendação de forma clara e técnica.",
        "Você deve somente verificar e corrigir problemas de segurança, sem alterar a funcionalidade original do código.",
        "Retorne apenas o texto formatado em Markdown, sem tentar salvar arquivos locais."
        ]
)