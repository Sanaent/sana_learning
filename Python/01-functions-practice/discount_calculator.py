def calculator_discount(price, percent):
    return price - (price * percent) // 100


price = int(input("price: "))
percent = int(input("discount %: "))

print(calculator_discount(price, percent))