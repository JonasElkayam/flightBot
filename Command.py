from telegram import Update
from telegram.ext import ContextTypes
from utils.keyboards import set_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הגעת למקום הנכון לטיסה הבאה שלך 🚀😎")
    await set_keyboard(update, context)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("כרגע הבוט רק מחזיר לך את מה שאתה רושם לו")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text("the message you sent is: " + user_message)
