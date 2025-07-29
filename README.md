# 🌦️ Telegram Weather Bot

A simple Telegram bot that provides current weather information for any city using the [OpenWeatherMap API](https://openweathermap.org/api). Built with Python and [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

---

## 🚀 Features

- Get real-time weather by city name
- Shows temperature, weather description, humidity, wind speed
- Includes the timestamp of the latest data update

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/weather_bot.git
cd weather_bot
```

2. **Install required libraries:**

```bash
pip install pyTelegramBotAPI requests
```

---

## 🔐 Configuration

1. Get your **Telegram Bot Token** from [@BotFather](https://t.me/BotFather)
2. Get your **API key** from [OpenWeatherMap](https://openweathermap.org/)
3. Replace the placeholders in `weather_bot.py`:

```python
TBOT_API_TOKEN = "your_telegram_token"
API_key = "your_openweather_api_key"
```

---

## ▶️ Usage

Run the bot:

```bash
python weather_bot.py
```

In Telegram:
- Send `/start` to begin
- Use `/weather` and then type a city name

---

## 📁 Files

```
weather_bot/
├── bot.py           # Main bot script
├── requirements.txt # Optional: to list dependencies
├── README.md        # Project description
```

---

## 💬 Example

```
User: /weather  
Bot: Write the city you are interested in  
User: Kyiv  
Bot: Now weather in Kyiv: 23°C, broken clouds, 78% humidity, 1.5km/h wind.  
Last time info update: 2025-07-23 19:00
```

---

## 📜 License

MIT License — free to use, modify and share.
