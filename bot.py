import os
import telebot
from telebot.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://web-production-05a2e.up.railway.app"  # Заменить на твой Railway URL

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = KeyboardButton("Открыть торговлю", web_app=WebAppInfo(url=WEBAPP_URL))
    markup.add(webapp_btn)
    bot.send_message(message.chat.id, "Нажми кнопку ниже, чтобы открыть Mini App 👇", reply_markup=markup)

bot.infinity_polling()
