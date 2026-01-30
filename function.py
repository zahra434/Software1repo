#Function
#Exercise 1
import random
def roll_dice():
    return random.randint(1, 6)
result = 0
while result != 6:
    result = roll_dice()
    print(result)


#Exercise 2
import random
def roll_dice(sides):
    return random.randint(1, sides)
max_number = int(input("Enter the maximum number on the dice: "))
result = 0
while result != max_number:
    result = roll_dice(max_number)
    print(result)


#Exercise 3
def gallons_to_liters(gallons):
    return gallons * 3.785
g = float(input("Enter gallons: "))
liters = gallons_to_liters(g)
print(liters)


#Exercise 4
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
nums = [3, 6, 1, 10]
result = sum_list(nums)
print(result)


#Exercise 5
def remove_odd(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list
nums = [3, 6, 1, 10]
result = remove_odd(nums)
print("Original list: ", nums)
print("New list: ", result)


#Exercise 6
import math
def pizza_unit_price(diameter_cm,price_euro ):
    radius = diameter_cm / 2
    area_cm2 = math.pi * radius * radius
    area_m2 = area_cm2 / 1000
    unit_price = price_euro / area_m2
    return unit_price
d1 = float(input("Enter the diameter of the pizza (cm): "))
p1 = float(input("Enter the price of the pizza 1 (euro): "))
d2 = float(input("Enter the diameter of the pizza 2 (cm): "))
p2 = float(input("Enter the price of the pizza 2 (euro): "))
unit1 = pizza_unit_price(d1,p1)
unit2 = pizza_unit_price(d2,p2)
if unit1 < unit2:
    print("Pizza 1 is better value for money")
else:
    print("Both pizzas have the same value")




