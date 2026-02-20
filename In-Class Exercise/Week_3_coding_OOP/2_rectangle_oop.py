# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# rect1 = Rectangle(5,3)
# print(rect1.area())
# rect2 = Rectangle(8,4)
# print(rect2.area())

# Exercise 2: Circle class
# attribute -> radius
# method -> area() ->3.14 * r * r

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
circle1 = Circle(5)
print(circle1.area())