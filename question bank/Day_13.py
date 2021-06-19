# Question 47
# > **_Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area._**
# > **_Use def methodName(self) to define a method._**
# import math
# class Circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return self.radius**2*math.pi
# a=Circle(10)
# print(a.area())


# Question 48
# > **_Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area._**
# > **_Use def methodName(self) to define a method._**
# class Rectangle():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# a=Rectangle(5,10)
# print(a.area())


# Question 49
#  **_Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default._**
# > **_To override a method in super class, we can define a method with the same name in the super class._**
class Shape():
    # def __init__(self):
    #     pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        # Shape.__init__(self)
        self.length=length
    def area(self):
        return self.length**2
a=Square(5)
print(a.area())     # prints 25 as given argument


# Question 50
# > **_Please raise a RuntimeError exception._**
# > **_UUse raise() to raise an exception._**
raise RuntimeError('something wrong')



