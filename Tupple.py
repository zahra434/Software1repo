#Tupple, Set , Dictionary
#Exercise 1
seasons = ("Winter", "Spring", "Summer", "Autumn")
month = int(input("Enter month number(1-12): "))
if month ==12 or month ==1 or month ==2:
    print(seasons[0])
elif month ==3 or month ==4 or month ==5:
    print(seasons[1])
elif month ==6 or month ==7 or month ==8:
    print(seasons[2])
elif month ==9 or month ==10 or month ==11:
    print(seasons[3])
else:
    print("Invalid month ")

#Exercise 2
names = set()
while True:
    name = input("Enter a name: ")
    if name =="":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("All names:")
for n in names:
    print(n)

#Exercise 3
airports = {}
while True:
    print("1: Add new airport")
    print("2: Fetch airport information")
    print("3: Quit")
    user_input = int(input(" Choose an option"))
    if user_input == 1:
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print("Airport added")
    elif user_input == 2:
        code = input("Enter ICAO code: ")
        if code in airports:
            print("Airport name: ", airports[code])
        else:
            print("Airport not found")
    elif user_input == 3:
        print("Goodbye")
        break
    else:
        print("Invalid user input")

