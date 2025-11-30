# Flask Chatbot with Socket.IO and AI

This project is a real-time Chatbot built with Python (Flask) and Socket.IO. It features a modern web interface and integrates with an external Artificial Intelligence API to respond to user messages.

📋 Features

Real-time Communication: Uses WebSockets for instant message sending and receiving.

Responsive Interface: Clean and adaptable design (CSS included).

Markdown Formatting: AI responses support formatting (bold, lists, code) rendered via marked.js.

Chat History: The chat maintains message history for the current session.

Secure Configuration: Uses environment variables (.env) to protect API keys.

🚀 How to Run the Project Locally

1. Prerequisites

Make sure you have Python 3.x installed on your machine.

2. Installation

Open your terminal in the project's root folder and install the dependencies:

pip install -r requirements.txt


Note: Alternatively, you can install the packages directly:

pip install flask flask-socketio requests python-dotenv


3. Configuration (.env)

The .env file is used to store sensitive configurations that should not be shared publicly (such as passwords and tokens).

Create a file named .env in the backend/ folder (or in the root, wherever app.py is located).

Copy the content below and paste it into the file:

# Flask Secret Key (can be any secure random text)
SECRET_KEY=your_super_secure_secret_key

# AI API URL
API_TOKEN_URL=[https://api.example.com/v1/chat](https://api.example.com/v1/chat)

# Your API Authentication Token
API_TOKEN_AGENT_AI=your_token_here_12345


Important: Replace https://api.example.com/v1/chat and your_token_here_12345 with your actual AI API credentials.

4. Running the Chatbot

In the terminal, navigate to the folder containing the app.py file (usually backend/) and run:

python app.py


If successful, you will see a message indicating the server is running. Open your browser and access:

http://127.0.0.1:5000

☁️ Deployment

To deploy your chatbot for public use, do not use the development server (python app.py). You will need a production server setup.

Recommended Option: Render or Railway

Platforms like Render or Railway are excellent for Python projects utilizing Socket.IO.

Create a file named Procfile (no extension) in the project root with the following content (requires gunicorn and eventlet):

web: gunicorn --worker-class eventlet -w 1 backend.app:app


(Note: Adjust backend.app:app depending on your folder structure. If app.py is in the root, use just app:app).

In your hosting service:

Connect your GitHub repository.

Add the Environment Variables (the same keys from your .env) in the hosting configuration panel.

The start command will be automatically detected from the Procfile.
