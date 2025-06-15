import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tonconnect-manifest.json')
def manifest():
    return send_from_directory('.', 'tonconnect-manifest.json')

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
