import Command
import os
from dotenv import load_dotenv
from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application , CommandHandler, MessageHandler , filters , ContextTypes

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if TELEGRAM_BOT_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

async def set_commands(app):
    commads = [
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Get help with the bot"),
    ]
    await app.bot.set_my_commands(commads) 


async def set_keyboard(update: Update):
    keyboard = [
        [InlineKeyboardButton("✈️חפש טיסה", callback_data='search')],
        [InlineKeyboardButton("👩🏻‍🔧 קבל עזרה", callback_data='help')],
        [InlineKeyboardButton("↪️חזור לתפריט הראשי", callback_data='start')],
    ]
    replay_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(" ➡️📋בחר אפשרות: ", replay_markup=replay_markup)

# async def search():

    

def main():
    app = Application.builder().token("TELEGRAM_BOT_TOKEN").post_init(set_commands).build()

    app.add_handler(CommandHandler("start", Command.start))
    app.add_handler(CommandHandler("help", Command.help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , Command.echo))

    # asyncio.run(set_commands(app))

    app.run_polling()
    

if __name__ == '__main__':
    main()
