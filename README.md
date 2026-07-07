Verificador de Código IA

# Visão Geral
O "Verificador de Código IA" é uma aplicação web construída utilizando o framework Streamlit. O sistema permite que os usuários colem um trecho de código e escolham entre três funcionalidades: gerar um arquivo README.md, analisar a segurança do código, ou otimizar a performance do código. A aplicação integra três agentes inteligentes, cada um especializado em uma dessas áreas.

# Funcionalidades
- Gerar README.md: Cria uma documentação do códigocom base no que foi colado pelo usuário.
- Analisar Segurança: Verifica o código em busca de vulnerabilidades de segurança.
- Otimizar Performance: Analisa o código e sugere melhorias para otimização de performance.
  
# Estrutura do Código
Importação de Módulos: O código importa bibliotecas essenciais como streamlit, os, dotenv e módulos personalizados que implementam os agentes para documentação, performance e segurança.

Carregamento das Chaves de API: O uso do dotenv permite carregar variáveis de ambiente, como chaves de API que podem ser necessárias para a execução dos agentes.

Configuração da Página do Streamlit: Configura o título, ícone e layout da interface do usuário.

Menu Lateral: O usuário pode escolher o que deseja fazer a partir de um menu lateral que apresenta três opções.

Área Principal de Input: É apresentada uma área onde o usuário pode colar seu código.

Execução da Análise: Dependendo da opção escolhida, a função executar_analise é chamada, que processa o código e utiliza os agentes correspondentes para gerar os resultados desejados.

# Requisitos
Para executar este sistema, você precisará das seguintes bibliotecas e dependências:

- streamlit
- python-dotenv
- Módulos personalizados:
  documentador (deve conter a classe agente_documentacao)
  performance (deve conter a classe agente_performance)
  seguranca (deve conter a classe agente_seguranca)

# Como instalar as dependências
Você pode instalar as bibliotecas necessárias usando os seguintes comandos em seu terminal:

No Linux
pip install streamlit python-dotenv
No Windows
pip install streamlit python-dotenv
Passo a Passo para Rodar o Código
Clone o repositório ou gere um novo arquivo Python (verificador_codigo.py) e cole o código fornecido nele.

Instale as dependências conforme as instruções acima.

Crie um arquivo .env na raiz do diretório do seu projeto, e adicione suas chaves de API necessárias, caso sejam requeridas pelos agentes.

Execute a aplicação Streamlit digitando o seguinte comando no terminal:

No Linux e Windows
streamlit run verificador_codigo.py
Abra o navegador: Após executar o comando, siga o link que aparecerá no terminal (normalmente http://localhost:8501) para acessar a aplicação.

Utilize a aplicação: Cole seu código na área designada, selecione uma opção no menu lateral e clique no botão "Executar" para ver os resultados.

Conclusão
O "Verificador de Código IA" é uma ferramenta prática e poderosa para desenvolvedores que buscam aprimorar seus códigos através de documentação, segurança e performance, utilizando inteligência artificial como suporte. A configuração é simples e a interface intuitiva facilita a experiência do usuário.
