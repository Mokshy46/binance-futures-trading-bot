
def validate_side(side):
    if side != "BUY" and side != "SELL":
        raise ValueError("Invalid side. Allowed values: BUY, SELL")

    
    
def validate_order_type(order_type):
    
    if order_type != "MARKET" and order_type != "LIMIT":
        raise ValueError("Invalid order type. Allowed values: MARKET, LIMIT")

    
def validate_quantity(quantity):
    if quantity <=0 :
        raise ValueError("Quantity must be greater than 0")


def validate_price(order_type, price):
    if order_type == "MARKET" and price == None:
        return
    
    if order_type == "LIMIT":

        if price is None:
            raise ValueError("LIMIT orders require a price")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        return