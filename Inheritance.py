# Exersice 1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name : {self.name}\n Author : {self.author} \n Page count : {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information11(self):
        print(f" Magazine name : {self.name} \n Chief editor : {self.chief_editor}")


book = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyyppa")

book.print_information()
magazine.print_information11()


# Exercise 2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def drive(self, hours):
        self.distance_travelled += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.current_speed = 120
gasoline_car.current_speed = 100

electric_car.drive(3)
gasoline_car.drive(3)

print("Electric car distance:" , electric_car.distance_travelled, "km")
print("Gasoline car distance:" , gasoline_car.distance_travelled, "km")

