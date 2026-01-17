# Module 2 Exercise 1
name=input("What is your name? ")
print("Hello," ,name + "!")

#Exercise 2
import math
radius=float(input("Enter the radius of the circle: "))
area=math.pi*radius**2
print("The area of the circle is",area)

#Exwercise 3
length = float(input("Enter the length of the circle: "))
width = float(input("Enter the width of the circle: "))
perimeter=2*(length+width)
area = length*width
print("Premeter:" , perimeter)
print("Area:" , area)

#Exercise 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
sum_numbers=a+b+c
product = a*b*c
average = sum_numbers/ 3
print("The sum is", sum_numbers)
print("The product is", product)
print("The average is", average)

#Exercise 5
talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_grams = (talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3)
kilograms = int(total_grams / 1000)
grams = total_grams % 1000
print(f'The weight is{kilograms} kilograms and {grams:.2f} grams.' )

#Exercise 6
import random
digit_three_1 = random.randint(0,9)
digit_three_2 = random.randint(0,9)
digit_three_3 = random.randint(0,9)
digit_four_1 = random.randint(0,6)
digit_four_2 = random.randint(0,6)
digit_four_3 = random.randint(0,6)
digit_four_4 = random.randint(0,6)
print(f"3-digit code:\n {digit_three_1}{digit_three_2}{digit_three_3}")
print(f"4-digit code:\n {digit_four_1}{digit_four_2}{digit_four_3}{digit_four_4}")






