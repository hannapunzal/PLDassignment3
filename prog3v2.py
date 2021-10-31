import math
def money():
    _money = int(input("Enter the amount of money you have: "))
    return _money

def apple():
    _apple = int(input("Enter apple price: "))
    return _apple

def operation2(moneyF, appleF):
    apple_total = moneyF/appleF
    return apple_total

def operation(moneyF, appleF):
    apple_quant = int(moneyF/appleF)
    cost_total = apple_quant*appleF
    money_change = moneyF - cost_total
    return money_change

moneyq = money()
appleq = apple()
total = math.floor(operation2(moneyq,appleq))
change = float(operation(moneyq, appleq))
print(f"You can buy {total} apples and your change is PHP{change}. Thank you!")