#Exercise 1 & 2
class   Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is now at floor {self.current_floor}")
    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))
    def run_elevators(self, elevator_num, target_floor):
        print(f"---Moving elevator{elevator_num}---")
        self.elevators[elevator_num].go_to_floor(target_floor)
my_building = Building(1, 10, 3)
my_building.run_elevators(0, 5)

#Exercise 3
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            return
    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator reached floor {self.current_floor}")
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))
    def run_elevators(self, elevator_num, target_floor):
        print(f"Moving elevator{elevator_num}...")
        self.elevators[elevator_num].go_to_floor(target_floor)
    def fire_alarm(self):
        print("!!! FIRE ALARM !!! All elevators moving to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
my_building = Building(1, 10, 3)
my_building.run_elevators(0, 5)
my_building.run_elevators(1, 8)
my_building.run_elevators(2, 3)
my_building.fire_alarm()

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
class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list
    def hours_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    def print_status(self):
        print(f"\nRace:{self.name}")
        print(f"{'Reg Num':<10} | {'Max Speed':<10} | {'Distance':<10}")
        print("-" * 35)
        for car in self.cars:
            print(f"{car.reg_number:<10} | {car.max_speed:<10} | {car.travelled_distance:<10.1f}")
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
all_cars = []
for i in range(1, 11):
    max_s = random.randint(100, 200)
    all_cars.append(Car(f"ABC-{i}", max_s))
grand_race = Race("Grand Demolition Derby", 8000, all_cars)
hours_elapsed = 0
while not grand_race.race_finished():
    grand_race.hours_passes()
    hours_elapsed += 1
    if hours_elapsed % 10 == 0:
        print(f"Time Elapsed: {hours_elapsed} hours")
        grand_race.print_status()
print(f"\n---RACE FINISHED after {hours_elapsed} hours---")
grand_race.print_status()


