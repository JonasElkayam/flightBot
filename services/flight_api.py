import os
from telegram import Update
from telegram.ext import ContextTypes
import requests as request

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")


async def search_flights_api(update: Update, context: ContextTypes.DEFAULT_TYPE, origin, destination, flight_date) -> None:
    
    headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST,
            "Accept": "application/json" 
        }

    params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": flight_date, 
            "date_to": flight_date,   
            "partner": "picky", 
            "limit": 5,        
            "curr": "ILS",     
            "adults": 1       
            # "return_from": "DD/MM/YYYY",
            # "return_to": "DD/MM/YYYY",
        }
    
    try:
        response = await request.get(
            url="https://kiwi-com.p.rapidapi.com/flights",
            headers=headers,
            params=params
        )
        flight_data = response.json()
        if 'data' in flight_data and flight_data['data']:
            for flight_item in flight_data['data']:
                try:
                    price = flight_item.get('price', 'N/A')
                    deep_link = flight_item.get('deep_link', 'https://www.kiwi.com/') 
                    
                    outbound_leg = flight_item.get('route', [{}])[0]
                    
                    departure_time = outbound_leg.get('local_departure', 'לא ידוע')
                    arrival_time = outbound_leg.get('local_arrival', 'לא ידוע')
                    airline = outbound_leg.get('airline', 'לא ידוע')
                    flight_number = outbound_leg.get('flight_no', 'לא ידוע')
                    
                    message_text += (
                        f"✈️ **חברת תעופה:** {airline} (טיסה {flight_number})\n"
                        f"🕒 **יציאה:** {departure_time[11:16]} (מ-{outbound_leg.get('cityFrom', 'N/A')} - {outbound_leg.get('flyFrom', 'N/A')})\n"
                        f"🛬 **הגעה:** {arrival_time[11:16]} (ל-{outbound_leg.get('cityTo', 'N/A')} - {outbound_leg.get('flyTo', 'N/A')})\n"
                        f"💰 **מחיר:** {price} ILS\n"
                        f"🔗 [לצפייה בטיסה]({deep_link})\n\n"
                    )
                    flights_found = True
                except (IndexError, TypeError) as e:
                    
                    continue # נמשיך לפריט הבא אם יש בעיה בעיבוד הנוכחי
        
        if flights_found:
            await update.message.reply_text(message_text, parse_mode='Markdown')
        else:
            await update.message.reply_text(f"לא נמצאו טיסות מ-{origin} ל-{destination} בתאריך {flight_date}. נסה יעד או תאריך אחר.")

    
    except Exception as e:
        await update.message.reply_text(
            "אירעה שגיאה לא צפויה. אנא נסה שוב מאוחר יותר."
        )
