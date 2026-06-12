from bot.orders import place_order
from bot.validators import validate_side,validate_order_type,validate_price,validate_quantity
import argparse
from bot.logging_config import logger


parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

side = args.side.upper()
order_type = args.type.upper()
symbol = args.symbol.upper()
quantity = args.quantity
price = args.price

try:
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    validate_price(order_type, price)

    logger.info(
        f"Order Request: "
        f"symbol={symbol}, "
        f"side={side}, "
        f"type={order_type}, "
        f"quantity={quantity}, "
        f"price={price}"
    )

    response = place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )

    print("\n===== ORDER REQUEST =====")
    print(f"Symbol       : {symbol}")
    print(f"Side         : {side}")
    print(f"Type         : {order_type}")
    print(f"Quantity     : {quantity}")
    print(f"Price        : {price if price else 'N/A'}")

    print("\n===== ORDER RESPONSE =====")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    print("\n Order Processed Successfully ")


    logger.info(
        f"Order Response: "
        f"orderId={response.get('orderId')}, "
        f"status={response.get('status')}, "
        f"executedQty={response.get('executedQty')}, "
        f"avgPrice={response.get('avgPrice', 'N/A')}"
    )
except Exception as e:
    logger.error(str(e))
    print(e)