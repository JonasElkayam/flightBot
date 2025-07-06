import Command
import os
from dotenv import load_dotenv
from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application , CommandHandler, MessageHandler , filters , ContextTypes, CallbackQueryHandler
from utils.keyboards import set_keyboard
from handlers import search_flights 
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if TELEGRAM_BOT_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

async def set_commands(app):
    commads = [
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Get help with the bot"),
    ]
    await app.bot.set_my_commands(commads) 


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'start':
        await set_keyboard(update, context)  
    elif query.data == 'search':
        await query.edit_message_text("🔍 מחפש טיסה")
        await search_flights.search()
    elif query.data == 'help':
        await query.edit_message_text("👩🏻‍🔧 איך אפשר לעזור לך?")
    else:
        await query.edit_message_text("⚠️ פעולה לא מוכרת")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).post_init(set_commands).build()

    app.add_handler(CommandHandler("start", Command.start))
    app.add_handler(CommandHandler("help", Command.help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, Command.echo))
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("🤖 הבוט פועל...")
    app.run_polling()

if __name__ == '__main__':
    main()
