from telegram import Update
from telegram.ext import ContextTypes
from services.flight_api import search_flights_api as flight_api_search

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    origin = await update.callback_query.message.reply_text("Please enter the origin city:")
    destination = await update.callback_query.message.reply_text("Please enter the destination city:")
    flight_date = await update.callback_query.message.reply_text("Please enter the flight date (DD/MM/YYYY):")

    flight_api_search(update, context, origin, destination, flight_date)