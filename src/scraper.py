import asyncio
from playwright.async_api import async_playwright

class PriceScraper:
    def __init__(self, user_agent=None):
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

    async def fetch_price(self, url, selector):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent=self.user_agent)
            page = await context.new_page()
            
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                element = await page.wait_for_selector(selector, timeout=10000)
                price_text = await element.inner_text()
                # Extract numbers and dots only
                clean_price = float(''.join(c for c in price_text if c.isdigit() or c == '.'))
                return clean_price
            except Exception as e:
                print(f"Scraping Error: {e}")
                return None
            finally:
                await browser.close()