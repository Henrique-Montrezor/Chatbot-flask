from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
import requests
from dotenv import load_dotenv, find_dotenv

# 1. Carrega variáveis de ambiente
DOTENV_PATH = find_dotenv()
if DOTENV_PATH:
    load_dotenv(DOTENV_PATH)
else:
    load_dotenv()

# Caminho para templates
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Lógica para encontrar as pastas templates e static
if os.path.exists(os.path.join(BASE_DIR, 'templates')):
    template_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
elif os.path.exists(os.path.join(BASE_DIR, '..', 'templates')):
    template_dir = os.path.abspath(os.path.join(BASE_DIR, '..', 'templates'))
    static_dir = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))
else:
    # Último recurso: aponta para a própria pasta
    template_dir = BASE_DIR
    static_dir = os.path.join(BASE_DIR, 'static')

print(f"--- DEBUG CAMINHOS ---")
print(f"Base: {BASE_DIR}")
print(f"Templates: {template_dir}")
print(f"Static: {static_dir}")
print(f"----------------------")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret!')
io = SocketIO(app, cors_allowed_origins="*")

messages = []

# Configurações da API
_url_raw = os.environ.get('API_TOKEN_URL', '')
API_URL = _url_raw.strip().rstrip('/')
API_TOKEN = os.environ.get('API_TOKEN_AGENT_AI') 

def ask_agent_ai(mensagem_usuario):
    """
    Envia o texto para a API externa e retorna a resposta limpa.
    """
    if not API_URL or not API_TOKEN:
        return "⚠️ **Erro de configuração:** URL ou Token da API não encontrados no `.env`."

    try:
        body = {
            "assistantId": "1764179347569-74c0cb9f-0a2c-479a-8d48-0dc9c01a1a02",
            "prompt": mensagem_usuario,
            "responseFormat": "markdown"
        }

        headers = {
            "x-api-key": API_TOKEN.strip(), 
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        
        print(f"--- ENVIANDO PARA IA ---")
        response = requests.post(API_URL, json=body, headers=headers, timeout=40) 
        
        if response.status_code == 200:
            data = response.json()
            print(f"Resposta bruta da API: {data}") # Log para debug
            
            # Lógica de extração atualizada para pegar o 'message'. Prioriza 'message', depois 'content', depois 'response'
            return data.get('message', data.get('content', data.get('response', str(data))))
            
        else:
            return f"❌ **Erro na API** ({response.status_code}): {response.text}"

    except requests.exceptions.Timeout:
        return "⏱️ A IA demorou muito para responder."
    except Exception as e:
        print(f"Erro: {e}")
        return f"🐛 **Erro interno:** `{str(e)}`"

@app.route('/')
def home():
    return render_template('index.html')

@io.on('sendMessage')
def handle_send_message(msg):
    print(f"Mensagem de {msg['name']}: {msg['message']}")
    messages.append(msg)
    emit('getMessage', msg, broadcast=True)

    # Lógica de Resposta do Bot
    texto_usuario = msg.get('message', '').lower().strip()
    resposta_servidor = None

    if msg['name'] != 'Sistema':
        if texto_usuario == 'ajuda':
            resposta_servidor = """
### Comandos Disponíveis:
* `ajuda`: Mostra esta mensagem.
* `status`: Verifica conexão.
* **Qualquer outra coisa**: Conversa com a **Agente AI**.
            """
        elif texto_usuario == 'status':
            resposta_servidor = "✅ Sistema online. Conectado à agente AI."
        else:
            resposta_servidor = ask_agent_ai(msg['message'])

    if resposta_servidor:
        bot_msg = {'name': 'Sistema', 'message': resposta_servidor}
        messages.append(bot_msg)
        emit('getMessage', bot_msg, broadcast=True)

@io.on('getHistory')
def handle_get_history():
    emit('history', messages)

if __name__ == '__main__':
    io.run(app, debug=True, allow_unsafe_werkzeug=True)