from flask import Flask, request, jsonify
import requests
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
BOT_TOKEN = os.getenv('BOT_TOKEN')

@app.route('/api/custom_method', methods=['POST'])
def handle_custom_method():
    """Обработчик кастомных методов из TMA"""
    try:
        data = request.get_json()
        logger.info(f"📨 Received API request: {data}")
        
        if not data or 'method' not in data:
            return jsonify({'error': 'Missing method name'}), 400
        
        method_name = data.get('method')
        params = data.get('params', {})
        
        logger.info(f"🔧 Processing method: {method_name}")
        logger.info(f"📋 Params: {params}")
        
        if method_name == 'send_message_to_user':
            return send_message_to_user(params)
        elif method_name == 'ping':
            return jsonify({'status': 'success', 'message': 'pong'})
        else:
            logger.error(f"❌ Unknown method: {method_name}")
            return jsonify({'error': 'Unknown method'}), 404
            
    except Exception as e:
        logger.error(f"💥 Server error: {e}")
        return jsonify({'error': str(e)}), 500

def send_message_to_user(params):
    """Отправка сообщения через Telegram Bot API"""
    try:
        to_user = params.get('to_user')
        message_text = params.get('message')
        from_user = params.get('from_user', 'Anonymous')
        
        logger.info(f"👤 Sending message to: {to_user}")
        logger.info(f"💬 Message: {message_text}")
        
        if not to_user or not message_text:
            return jsonify({'error': 'Missing to_user or message'}), 400
        
        # Формируем текст сообщения
        text = f"📨 Сообщение от {from_user}:\n\n{message_text}"
        
        # Отправляем через Telegram Bot API
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': to_user,
            'text': text,
            'parse_mode': 'HTML'
        }
        
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code == 200:
            logger.info("✅ Message sent successfully")
            return jsonify({
                'status': 'success', 
                'message': 'Message sent successfully'
            })
        else:
            error_msg = response.json().get('description', 'Unknown error')
            logger.error(f"❌ Telegram API error: {error_msg}")
            return jsonify({
                'status': 'error', 
                'message': f'Telegram API error: {error_msg}'
            }), 500
            
    except Exception as e:
        logger.error(f"❌ Send message error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Проверка здоровья API"""
    return jsonify({
        'status': 'healthy', 
        'service': 'TMA API',
        'bot_token_set': bool(BOT_TOKEN)
    })

@app.route('/')
def index():
    return jsonify({'message': 'Flask API is running'})

if __name__ == '__main__':
    logger.info("🚀 Starting Flask API on 0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)