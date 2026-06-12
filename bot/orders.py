from bot.client import client
from bot.validators import validate_side

def place_order(symbol, side,order_type, quantity, price=None):

    if order_type =="MARKET":
        return client.futures_create_order(
        symbol=symbol,
        type = order_type,
        side=side,
        quantity=quantity,
    )
    
    elif order_type =="LIMIT":           
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type = order_type,
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
    
    else :
        raise ValueError("Unsupported Order Type")
    
