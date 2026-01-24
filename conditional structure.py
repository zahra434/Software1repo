#Conditional exercise

#number one
length = int(input("Enter the length of the zander (cm): "))
if length >= 42:
    print("Congratulations, the zander meet the size limit.")
else:
    missing = 42 - length
    print("Release the fish back into the lake. ")
    print("The fish is" , missing , "cm below the size limit. ")


#number two
user = input("Enter the cabin class: ")
if user == "LUX" :
    print('Upper_deck cabin with a balcony.')
elif user == "A" :
    print("Cabin above the car deck, equipped with a window.")
elif user == "B" :
    print("Windowless cabin above the car deck.")
elif user == "C" :
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#Number 3
gender = input("Enter biological gender (female/male): ")
hb = int(input("Enter hemoglobin value (g/l): "))
if gender == "female":
    if hb < 117 :
        print("Hemoglobin is low for females.")
    elif hb <= 155 :
        print("Hemoglobin is normal for females.")
    else:
        print("Hemoglobin is high for females.")
elif gender == "male":
    if hb <134 :
        print("Hemoglobin is low for males.")
    elif hb <= 167 :
        print("Hemoglobin is normal for males.")
    else:
        print("hemoglobin is high for males.")

#Number 4
year = int(input("Enter a year: "))
if  year / 100 == 0:
    if year / 400 == 0:
        print("Leap year. ")
    else:
        print("Not a leap year. ")
elif year / 4 == 0:
    print("Leap year.")
else:
    print("Not a leap year. ")




