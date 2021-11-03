
def appleQ():
     apple_Question = int(input("How many apples do you want to buy? "))
     return apple_Question

def orangeQ():
    orange_Question = int(input("How many oranges do you want to buy? "))
    return orange_Question

def operation(appleF, orangeF):
    apple_total = appleF*apple_price
    orange_total = orangeF*orange_price
    sum = apple_total + orange_total
    return sum

apple_price = 20
orange_price = 25

apples = appleQ()
oranges = orangeQ()
total = operation(apples, oranges)

print(f"Hi, The total amount for the apples and oranges is PHP{total: .2f}. Thank you!")