from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

def build_keyboard():
    keyboard = [
        [InlineKeyboardButton("✈️ חפש טיסה", callback_data='search')],
        [InlineKeyboardButton("👩🏻‍🔧 קבל עזרה", callback_data='help')],
        [InlineKeyboardButton("↪️ חזור לתפריט הראשי", callback_data='start')],
    ]
    return InlineKeyboardMarkup(keyboard)

async def set_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = build_keyboard()

    if update.message:
        await update.message.reply_text("➡️📋 בחר אפשרות:", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text("➡️📋 בחר אפשרות:", reply_markup=reply_markup)
