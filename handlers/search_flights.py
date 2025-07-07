from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters
from services.flight_api import search_flights_api as flight_api_search

ORIGIN, DESTINATION, DATE, FIN = range(4)

async def cancel(update, context):
    await update.message.reply_text("שיחה בוטלה.")
    return ConversationHandler.END

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("בחר עיר מוצא:")
    return ORIGIN

    # flight_api_search(update, context, origin, destination, flight_date)

async def get_origin(update, context):
    context.user_data["origin"] = update.message.text
    await update.message.reply_text("בחר יעד: ")
    return DESTINATION

async def get_dest(update, context):
    context.user_data["destination"] = update.message.text
    await update.message.reply_text("באיזה תאריכים?")
    return DATE

async def get_date(update, context):
    context.user_data["date"] = update.message.text
    await update.message.reply_text("מעולה")
    return FIN

async def pass_data_to_api(update, context):
    origin = context.user_data["origin"]
    destination = context.user_data["destination"]
    flight_date = context.user_data["date"]

    flight_api_search(update, context, origin, destination, flight_date)
    return ConversationHandler.END

conv_hendler = ConversationHandler(
    entry_points=[CommandHandler("search", search)],
    states={
        ORIGIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_origin)],
        DESTINATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_dest)],
        DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_date)],
        FIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, pass_data_to_api)],
    },
    fallbacks=[CommandHandler("cancel", cancel)]
)