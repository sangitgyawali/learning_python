# Functions in python

def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(100, 0.2, 0.1))