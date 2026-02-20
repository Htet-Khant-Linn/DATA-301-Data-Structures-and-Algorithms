# PascalCase = UserProfile is used for Class
# camelCase = userProfile is used for variables and function
# snake_case = user_profile is used for variables


# class Student:
#     def __init__(self, name, age): # __init__, __init__(student1, "Alice", 20)
#         self.name = name # name = name, self.name -> student1.name = 'Alice'
#         self.age = age

#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} year old.")

# # student1 = Student("Alice", 20)
# student2 = Student("Bob", 25)

# student2.introduce()

# Exercise 1: Car class
# attributes -> brand and speed
# method() -> drive() -> "The {brand} car is driving at {speed}km/h."

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"The {self.brand} car is driving at {self.speed}km/h.")


car1 = Car("Toyota", 120)
car1.drive()