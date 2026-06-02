import telebot
import os

TOKEN = os.getenv("8696928675:AAGoDN_HivSyfelUtvJeY9kvs04bMV9OXCE")
bot = telebot.TeleBot(TOKEN)

user_xp = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot started!")

@bot.message_handler(commands=['rank'])
def rank(message):
    uid = message.from_user.id
    xp = user_xp.get(uid, 0)
    bot.reply_to(message, f"Your XP: {xp}")

@bot.message_handler(func=lambda m: True)
def add_xp(message):
    uid = message.from_user.id
    user_xp[uid] = user_xp.get(uid, 0) + 5

bot.infinity_polling()
