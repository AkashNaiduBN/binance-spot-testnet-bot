import logging
import os
from dotenv import load_dotenv
from bot import BasicBot
from utils import get_order_input

logging.basicConfig(
    filename='log/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()

def main():
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    bot = BasicBot(api_key, api_secret)

    symbol, side, order_type, quantity, price = get_order_input()
    result = bot.place_order(symbol, side, order_type, quantity, price)

    if result is not None:
        print("✅ Order placed successfully!")
        print(result)
    else:
        print("❌ Order placement failed. Check log/bot.log")

if __name__ == "__main__":
    main()
