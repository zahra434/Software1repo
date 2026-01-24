#Exercise while
#Number 1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

#Number two
while True:
    inches = float(input("Enter inches (negative number to quit): "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} inches = {cm:.2f}cm")

#Number3
numbers = []
value = input("Enter a number (empty to quit): ")
while value != "":
    numbers.append(float(value))
    value = input("Enter a number (empty to quit): ")
if numbers:
    print('smallest:', min(numbers))
    print('largest:', max(numbers))
else:
    print("No numbers entered")

#Number 4
import random
secret = random.randint(1, 10)
guess = 0
while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess > secret:
        print("too high")
    elif guess < secret:
        print("too low")
print("correct")

#Number 5
attempts = 0
while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")
    if username == "python" and password == "rule":
        print("Welcome")
        break
    else:
        print("Wrong credentials")
        attempts += 1
if attempts == 5:
    print("Access denied")

#Number 6
import random
N = int(input('How many random points?'))
inside = 0
count = 0
while count < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        inside += 1
    count += 1
pi = 4 * inside / N
print("Approximation of pi :", pi)


