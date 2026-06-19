class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        return "The " + self.color + " " + self.brand + " is driving!"

car1 = Car("Toyota Supra", "Red")
car2 = Car("BMW M3", "Blue")

print(car1.drive())
print(car2.drive())
