from telegram import Update
from telegram.ext import ContextTypes

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("Please enter the origin city:")
