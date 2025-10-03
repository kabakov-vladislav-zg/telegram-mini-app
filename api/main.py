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
def handle_custom_method():
  try:
    data = request.get_json()        
    return send_profile(data)         
  except Exception as e:
    return jsonify({'error': str(e)}), 500

def send_profile(data):
  try:
    ownerId = data.get('ownerId')
    ownerName = data.get('ownerName')
    userId = data.get('userId')
    userName = data.get('userName')
    userUsername = data.get('userUsername')
    profile = data.get('profile')

    profile=Profile(
      telegram=userUsername,
      name=profile.get('name'),
      nickname=profile.get('nickname'),
      birthday=profile.get('birthday'),
      eyecolor=profile.get('eyecolor'),
    )
    payloadProfile = {
      'chat_id': ownerId,
      'text': profile.to_text(),
      'parse_mode': 'HTML'
    }
    response1 = requests.post(TG_URL, json=payloadProfile, timeout=10)
    
    if response1.status_code == 200:
      payloadSuccess = {
        'chat_id': userId,
        'text': 'Анкета доставлена!',
        'parse_mode': 'HTML'
      }
      response2 = requests.post(TG_URL, json=payloadSuccess, timeout=10)

      if response2.status_code == 200:
        return jsonify({
          'status': 'success', 
          'message': 'Message sent successfully',
        })
      else:
        error_msg2 = response2.json().get('description', 'Unknown error')
        return jsonify({
          'status': 'success', 
          'message': f'Message sent successfully, but: {error_msg2}',
        })
    else:
      error_msg1 = response1.json().get('description', 'Unknown error')
      return jsonify({
        'status': 'error', 
        'message': f'Telegram API error: {error_msg1}',
      }), 500
        
  except Exception as e:
    return jsonify({'error': str(e)}), 500

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