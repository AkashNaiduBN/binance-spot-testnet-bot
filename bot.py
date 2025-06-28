from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        if testnet:
            self.client = Client(api_key, api_secret)
            self.client.API_URL = 'https://testnet.binance.vision/api'
        else:
            self.client = Client(api_key, api_secret)
        logging.info("Binance Spot client initialized in testnet mode.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.create_test_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.create_test_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            logging.info(f"Order simulated: {order}")
            return order
        except Exception as e:
            logging.error(f"Order failed: {str(e)}")
            return None
