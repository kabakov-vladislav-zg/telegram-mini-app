import os
import logging
import sys
import requests
from flask import Flask, request, jsonify

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
app = Flask(__name__)

@app.route('/api/custom_web_app_data', methods=['POST'])
def handle_custom_web_app_data():
  """
  Обработчик кастомных методов из TMA
  """
  try:
    # Проверяем Content-Type
    if not request.is_json:
      return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    print(f"request.get_json(): {request.get_json()}")
    
    # Проверяем обязательные поля
    if not data or 'method' not in data:
      return jsonify({'error': 'Missing method name'}), 400
    
    method_name = data.get('method')
    method_params = data.get('params', {})
    
    # Обрабатываем методы
    if method_name == 'send_message_to_user':
      return forward_message_to_bot(method_params)
    elif method_name == 'ping':
      return jsonify({'status': 'success', 'message': 'pong'})
    else:
      return jsonify({'error': 'Unknown method'}), 404
        
  except Exception as e:
    return jsonify({'error': f'Server error: {str(e)}'}), 500
  
def forward_message_to_bot(params):
  # Используем Telegram Bot API для отправки сообщения
  bot_token = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
  url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
  
  payload = {
    'chat_id': params['sender']['id'],
    'text': f"📨 Сообщение от пользователя:\n\n{params['message']}",
    'parse_mode': 'HTML'
  }
  
  response = requests.post(url, json=payload)
  
  if response.status_code == 200:
    return {'status': 'success', 'message': 'Message sent'}
  else:
    return {'status': 'error', 'message': 'Failed to send'}

if __name__ == '__main__':
  logging.info("🚀 Starting Flask API on 0.0.0.0:5000")
  app.run(host='0.0.0.0', port=5000, debug=False)
