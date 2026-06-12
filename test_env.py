from bot.orders import place_order

response = place_order(
    symbol="BTCUSDT",
    order_type=  "MARKET",
    side = "BUY",
    quantity=0.001,
)

print(response)