# Assignment week 3
#List and for structure
#exercise 1
import random
n = int(input("How many diec do you want to roll? "))
total = 0
for i in range(n):
    roll = random.randint(1, 6)
    print("Dice", i + 1, ":", roll)
    total += roll
print("Sum of dice:", total)


#exercise 2
numbers = []
while True:
    x = input("Enter a number (empty to quit): ")
    if x == "":
        break
    numbers.append(int(x))
numbers.sort(reverse=True)
print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)


#exwrcise 3
n = int(input("Enter an integer: "))
if n <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i ==0:
            is_prime = False
            break
    if is_prime:
             print("Prime number")
    else:
            print("Not a prime number")


#exercise 4
cities = []
for i in range(5):
    city = input("Enter city name: ")
    cities.append(city)
print("Cities:")
for city in cities:
    print(city)



