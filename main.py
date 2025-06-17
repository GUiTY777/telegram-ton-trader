import os
import threading
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Загружаем токен
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://web-production-05a2e.up.railway.app"

# === Flask ===
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tonconnect-manifest.json')
def manifest():
    return send_from_directory('.', 'tonconnect-manifest.json')

@app.route('/health')
def health():
    return "OK"

# === Telegram Bot ===
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    webapp_btn = InlineKeyboardButton("🚀 Открыть торговлю", web_app=WebAppInfo(url=WEBAPP_URL))
    markup.add(webapp_btn)
    bot.send_message(message.chat.id, "Нажми кнопку ниже, чтобы открыть Mini App 👇", reply_markup=markup)

# === Запуск ===
def run_flask():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

def run_bot():
    print("Polling started successfully.")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_bot()
# update to trigger deploy
