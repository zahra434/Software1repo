#Exercise1
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
new_car = Car("ABC-123", 142)
print(f"Registration:{new_car.reg_number}")
print(f"Max Speed:{new_car.max_speed} km/h")
print(f"Current Speed:{new_car.current_speed} km/h")
print(f"Travelled Distance:{new_car.travelled_distance} km")

#Exercise 2
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
            if self.current_speed < 0:
                self.current_speed = 0
my_car = Car("ABC-123", 142)
my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"Current speed after acceleration:{my_car.current_speed} km/h")
my_car.accelerate(-200)
print(f"Final speed after emergency brake: {my_car.current_speed} km/h")

#Exercise 3
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
my_car = Car("ABC-123", 142)
my_car.accelerate(60)
my_car.drive(1.5)
print(f"Registration number:{my_car.reg_number}")
print(f"Current Speed:{my_car.current_speed} km/h")
print(f"Total Travelled Distance:{my_car.travelled_distance} km")

#Exercise 4
import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
cars = []
for i in range (1, 11):
    max_s = random.randint(100, 200)
    new_car = Car(f"ABC-{i}", max_s)
    cars.append(new_car)
race_on = True
while race_on:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_on = False
print(f"{'Reg Num':10} | {'Max Speed':<10} | {'Distance':<10}")
print("-" *35)
for car in cars:
    print(f"{car.reg_number:<10} | {car.max_speed:<10} | {car.travelled_distance:<10.1f}")
