import telebot

# روی سرور فقط توکن لازمه و بس!
TOKEN = "8521459920:AAHt1qAMzRAsSfWcZO5UW42v69dacYPHUUk"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام کیان! Kiancore روی سرور با قدرت استارت خورد. 🚀🔥")

if __name__ == "__main__":
    print("Bot is running on the server...")
    bot.infinity_polling()