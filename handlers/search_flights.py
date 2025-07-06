from telegram import Update
from telegram.ext import ContextTypes

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✈️ Let's search for a flight!\nPlease enter the origin city:")
