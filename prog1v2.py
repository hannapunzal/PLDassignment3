def getname():
    _name = input("Enter your name: ")
    return _name

def getage():
    _age = input("Enter your age: ")
    return _age

def getaddress():
    _address = input ("Enter your address: ")
    return _address

def display(name, age, address):
    print(f"Hi, my name is {name}. I am {age} years old and I live in {address}.")
    
# steps
# ask for name then save to variable
name = getname()
# ask for age then save to variable
age = getage()
# ask for address then save to variable
address = getaddress()
# display (name, age, address)
display(name, age, address)