from flask import Flask, request, jsonify
import requests
import os
import logging
import sys
from models.profile import Profile

logging.basicConfig(
  level=logging.ERROR,
  format='%(asctime)s - %(levelname)s - %(message)s',
  stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
BOT_TOKEN = os.getenv('BOT_TOKEN')
TG_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/api/send_profile', methods=['POST'])
def handle_send_profile():
  data = request.get_json()
  if not data:
    return jsonify({
      'status': 'error', 
      'error': 'No JSON data provided',
    }), 400

  required_fields = ['ownerId', 'userId', 'userUsername', 'profile']
  missing_fields = [field for field in required_fields if not data.get(field)]
  if missing_fields:
    return jsonify({
      'status': 'error', 
      'error': f'Missing required fields: {", ".join(missing_fields)}',
    }), 400

  profile = data.get('profile')
  profile=Profile(
    userId=data.get('userId'),
    username=data.get('userUsername'),
    name=profile.get('name'),
    nickname=profile.get('nickname'),
    birthday=profile.get('birthday'),
    eyecolor=profile.get('eyecolor'),
  )

  return send_telegram_message(data.get('ownerId'), profile.to_text())


def send_telegram_message(chat_id: str, text: str, parse_mode: str = 'HTML') -> bool:
  try:
    payload = {
      'chat_id': chat_id,
      'text': text,
      'parse_mode': parse_mode
    }
    response = requests.post(TG_URL, json=payload, timeout=10)
    response.raise_for_status()
    return jsonify({
      'status': 'success', 
      'message': 'Message sent successfully',
    })
  
  except requests.exceptions.HTTPError as e:
    error_msg = e.response.json().get('description', 'Unknown Telegram error')
    return jsonify({
      'status': 'error', 
      'error': f'Telegram API error: {error_msg}',
      'data': payload,
    }), 500
      
  except requests.exceptions.RequestException as e:
    return jsonify({
      'status': 'error', 
      'error': f'Network error: {str(e)}',
    }), 503
      
  except Exception as e:
    return jsonify({
      'status': 'error', 
      'error': f'Unknown error: {str(e)}',
    }), 500

@app.route('/health', methods=['GET'])
def health_check():
  return jsonify({
    'status': 'healthy', 
    'service': 'API',
  })

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    port=5000,
    debug=False
  )