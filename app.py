from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system("cd /home/web-sekolah && git pull")
    return "Updated", 200


app.run(host='0.0.0.0', port=5000)
