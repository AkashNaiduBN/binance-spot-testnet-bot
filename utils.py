def get_order_input():
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None
    if order_type == 'LIMIT':
        price = float(input("Enter price: "))
    return symbol, side, order_type, quantity, price
