# Question 44
#_Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)._**
# print(list(map(lambda x:x**2,range(1,21))))


# Question 45
# > **_Define a class named American which has a static method called printNationality._**
# > **_Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this [link](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/)._**
# class American():
#     @staticmethod
#     def printNationality():
#         print('USA')
# American.printNationality()
# boy=American()
# boy.printNationality()


# Question 46
# > **_Define a class named American and its subclass NewYorker._**
# > **Use class Subclass(ParentClass) to define a subclass.\***
class American():
    def aa(self):
        print('aaa')
class NewYorker(American):
    def bb(self):
        print('bbb')
gg=NewYorker()
gg.bb()
gg.aa()