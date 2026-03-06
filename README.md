# 📉 AI-Powered Price Tracker & Discord Bot

An automated web scraper built with **Python** and **Playwright** that monitors product prices and sends real-time alerts to Discord when a target price is met.

## ✨ Features
* **Headless Scraping:** Uses Playwright to bypass basic bot detection.
* **Discord Integration:** Real-time notifications via `discord.py`.
* **Scheduled Checks:** Runs every 6 hours (configurable).
* **Price History:** (Optional) Logs data to SQLite.

## 🛠️ Setup
1. Clone the repo: `git clone https://github.com/yourusername/price-tracker-bot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Install Chromium: `playwright install chromium`
4. Add your Discord Token to a `.env` file.
5. Run the bot: `python src/bot.py`
