# from back import (
#     sum_number,
#     MAX_VALUE,
#     apple
# )
# sum_number(20,20)
# print(MAX_VALUE)
# print(apple)

def deco(f):
    print("func() was called")
    return f

@deco
def func(x):

    def main(num):
        print(num**2)
    main(x)

    return f"x = {x}"
print(func(10))


# enharitance
# incopsulatsiya
# palimafizm
# opi


class MyClass:
    """this is first class in the Python"""
    # object ni atribute va methodlari
    pass


class Car:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model 
        self.price = price

    def signal(self):
        print(self.name, "signal cholyapti")
car1 = Car("Damas", "chevrolet", 14000)
car2 = Car("Tesla", "Elon", 99999)

print(car1.name)
print(car1.model)
print(car1.price)
print(car2.name)


getattr()
setattr()
delattr()

