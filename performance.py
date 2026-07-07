from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
import dotenv
dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

agente_performance = Agent(
    name="Engenheiro de Performance",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    instructions=[
        "Você atua como um engenheiro de performance.",
        "Todo código que você receber, analise a velocidade da resposta e a memória que ele está ocupando.",
        "Se for o caso de poder substituir o código por algo mais otimizado, refatore o código e devolva o novo.",
        "IMPORTANTE: Não mude a funcionalidade original do código, focando somente em melhorar velocidade e memória.",
        "Você deve explicar o que melhorou de forma clara e técnica, mostrando os ganhos dessa melhora.",
        "Retorne apenas o texto formatado em Markdown, sem tentar salvar arquivos locais."
    ]
)