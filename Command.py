from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application , CommandHandler, MessageHandler , filters , ContextTypes

# command function
async def start(update: Update , context: ContextTypes):
    await update.message.reply_text("הגעת למקום הנכון לטיסה הבאה שלך 🚀😎")

async def help(update: Update , context: ContextTypes):
    await update.message.reply_text("כרגע הבוט רק מחזיר לך את מה שאתה רושם לו")

async def echo(update: Update , context: ContextTypes):
    user_message = update.message.text   
    await update.message.reply_text("the message you sent is: " + user_message)