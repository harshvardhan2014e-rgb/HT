class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

rect = Rectangle(5, 10)
print("Length:", rect.length)
print("Width:", rect.width)
print("Area:", rect.area())