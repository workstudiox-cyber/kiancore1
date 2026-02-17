import telebot
import os
from flask import Flask
from threading import Thread

# ۱. بخش زنده نگه داشتن (Keep Alive) برای اینکه رندر بات رو نخوابونه
app = Flask('')

@app.route('/')
def home():
    return "Kiancore is running like a beast! 🚀"

def run():
    # رندر از پورت ۸۰۸۰ یا پورت متغیری که خودش میده استفاده میکنه
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ۲. تنظیمات بات با استفاده از Environment Variable
# این همون جاییه که اگه ست نکنی، ارور ۴۰۱ میده
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام کیان! پروژه Kiancore با موفقیت روی سرور رندر مستقر شد. 🛠️🔥")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"دریافت شد: {message.text}")

if __name__ == "__main__":
    print("Initializing system...")
    keep_alive() # استارت سرور وب برای دور زدن محدودیت رایگان رندر
    print("Bot is polling...")
    bot.infinity_polling()
