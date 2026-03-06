📉 AI-Powered Price Tracker & Discord Alert Bot

An automated, serverless price monitoring system built with Python and Playwright. This tool tracks product price fluctuations, maintains a historical database using SQLite, and sends real-time alerts to Discord when deals are detected.

✨ Key Features

Stealth Scraping: Uses Playwright's headless browser with custom User-Agents to bypass basic anti-bot protections.

Historical Data: Logs every price check into a local SQLite database to track "All-Time Lows."

Serverless Execution: Runs 24/7 via GitHub Actions—no local server required.

Secure Credential Management: Utilizes GitHub Secrets and .env files to prevent API key exposure.

SQLi Protection: Implements parameterized queries for database interactions.

🏗️ Technical Architecture

The system operates in four distinct layers:

Extraction Layer: Playwright renders the page and uses CSS selectors to extract dynamic price data.

Storage Layer: SQLite stores price points with timestamps for trend analysis.

Logic Layer: Python compares current data against historical minimums and target thresholds.

Notification Layer: Discord's WebSocket API delivers the alert payload to the user.

🚀 Getting Started

1. Installation

# Clone the repository
git clone [https://github.com/your-username/price-tracker-bot.git](https://github.com/your-username/price-tracker-bot.git)
cd price-tracker-bot

# Install dependencies
pip install -r requirements.txt
playwright install chromium


2. Configuration

Create a .env file in the root directory:

DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=your_discord_channel_id


3. Usage

Update the configuration in src/bot.py with your target URL and CSS selector, then run:

python src/bot.py


☁️ Deployment (GitHub Actions)

This project is configured to run automatically every 6 hours.

Push your code to GitHub (ensure .env and prices.db are ignored).

Navigate to Settings > Secrets and variables > Actions.

Add DISCORD_TOKEN and CHANNEL_ID as Repository Secrets.

Enable Read and Write permissions under Actions > General > Workflow permissions to allow the bot to save price history back to the repo.

🛡️ Security Best Practices

As this project was developed with a Cybersecurity focus, it adheres to:

The Principle of Least Privilege: Discord bot permissions are restricted to "Send Messages" only.

Injection Prevention: Use of parameterized SQL queries to mitigate SQL Injection (SQLi) risks.

Secret Masking: Sensitive tokens are never hardcoded or checked into version control.

📄 License

Distributed under the MIT License.