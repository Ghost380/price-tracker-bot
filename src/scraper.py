import asyncio
from playwright.async_api import async_playwright

class PriceScraper:
    def __init__(self, url):
        self.url = url
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

    async def fetch_price(self, selector):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            # Create a context with a real user agent
            context = await browser.new_context(user_agent=self.user_agent)
            page = await context.new_page()
            
            await page.goto(self.url, wait_until="domcontentloaded")
            
            try:
                element = await page.wait_for_selector(selector, timeout=5000)
                price_text = await element.inner_text()
                # Clean the string (remove $, commas, etc)
                clean_price = float(''.join(c for c in price_text if c.isdigit() or c == '.'))
                return clean_price
            except Exception as e:
                print(f"Error scraping: {e}")
                return None
            finally:
                await browser.close()