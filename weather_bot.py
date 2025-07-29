import telebot
from telebot import types
import requests
from datetime import datetime
TBOT_API_TOKEN = "YOUR TOKEN HERE"
bot = telebot.TeleBot(TBOT_API_TOKEN)
API_key = "YOUR API KEY HERE"
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"👋 Hello! This bot shows the weather in any city.\nTo learn more, type /help.")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,"❓ To get weather info, type /weather and then enter the city name.")
@bot.message_handler(commands=["weather"])
def weather(message):
    bot.send_message(message.chat.id,"🌍 Please enter the city you are interested in:")
@bot.message_handler(content_types=["text"])
def get_weather(message):
    try:
        city = message.text.strip().capitalize()
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric")
        data = res.json()
        time_stamp = data['dt']
        time_zone = data['timezone']
        dt = datetime.utcfromtimestamp(time_stamp + time_zone)
        local_time = dt.strftime("%Y-%m-%d %H:%M")
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        bot.reply_to(
            message,
            f"📍 Weather in {city.capitalize()}:\n"
            f"🌡 Temperature: {temp}°C\n"
            f"☁️ Condition: {description}\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind: {wind_speed} km/h\n"
            f"🕒 Last update: {local_time}"
        )
    except:
        bot.send_message(message.chat.id,"⚠️ Sorry, I couldn't find that city.")
bot.polling()