# Chatbot Flask com Socket.IO e IA

Este projeto é um Chatbot em tempo real desenvolvido com Python (Flask) e Socket.IO. Ele possui uma interface web moderna e se integra a uma API externa de Inteligência Artificial para responder às mensagens dos usuários.

📋 Funcionalidades

Comunicação em Tempo Real: Uso de WebSockets para envio e recebimento instantâneo de mensagens.

Interface Responsiva: Design limpo e adaptável (CSS incluso).

Formatação Markdown: As respostas da IA suportam formatação (negrito, listas, código) renderizadas via marked.js.

Histórico de Chat: O chat mantém o histórico das mensagens na sessão atual.

Configuração Segura: Uso de variáveis de ambiente (.env) para proteger chaves de API.

🚀 Como Rodar o Projeto Localmente

1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina.

2. Instalação das Dependências

Abra o terminal na pasta raiz do projeto e execute:

pip install -r requirements.txt


Nota: ou instale diretamente com:
pip install flask flask-socketio requests python-dotenv

3. Configurando o .env (Variáveis de Ambiente)

O arquivo .env serve para guardar configurações sensíveis que não devem ser compartilhadas publicamente (como senhas e tokens).

Crie um arquivo chamado .env na pasta backend/ (ou na raiz, onde está o app.py).

Copie o conteúdo abaixo e cole no arquivo:

# Chave secreta do Flask (pode ser qualquer texto aleatório seguro)
SECRET_KEY=sua_chave_secreta_super_segura

# URL da API de Inteligência Artificial
API_TOKEN_URL=[https://api.exemplo.com/v1/chat](https://api.exemplo.com/v1/chat)

# Seu Token de autenticação da API
API_TOKEN_AGENT_AI=seu_token_aqui_12345


Importante: Substitua https://api.exemplo.com/v1/chat e seu_token_aqui_12345 pelos dados reais da sua API de IA.

4. Executando o Chatbot

No terminal, navegue até a pasta onde está o arquivo app.py (geralmente backend/) e execute:

python app.py


Se tudo der certo, você verá algo como:
Running on http://127.0.0.1:5000

Abra seu navegador e acesse: https://www.google.com/search?q=http://127.0.0.1:5000

☁️ Como Publicar (Deploy)

Para colocar seu chatbot online para que outras pessoas usem, você não deve usar o comando python app.py (que é apenas para desenvolvimento). Você precisará de um servidor de produção.

Opção Recomendada: Render ou Railway

Plataformas como Render ou Railway são ótimas para projetos Python com Socket.IO.

Crie um arquivo Procfile (sem extensão) na raiz do projeto com o seguinte conteúdo (necessário instalar gunicorn e eventlet):

web: gunicorn --worker-class eventlet -w 1 backend.app:app


(Nota: Ajuste backend.app:app dependendo da estrutura das suas pastas. Se app.py estiver na raiz, use apenas app:app).

No seu serviço de hospedagem:

Conecte seu repositório GitHub.

Adicione as Variáveis de Ambiente (as mesmas do .env) no painel de configuração da hospedagem.

O comando de inicialização será lido automaticamente do Procfile.

📂 Estrutura de Arquivos

/
├── backend/
│   ├── app.py           # Lógica do servidor Flask e Socket.IO
│   └── .env             # Arquivo de configuração (NÃO COMITAR NO GIT)
├── static/
│   └── css/
│       └── style.css    # Estilos da interface
├── templates/
│   └── index.html       # Interface do chat (HTML + JS Client)
├── requirements.txt     # Lista de dependências
└── README.md            # Documentação
