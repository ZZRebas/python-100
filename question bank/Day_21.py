# Question 85
# > **_By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]._**
# > **_Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple._**
# a=[12,24,35,70,88,120,155]
# print([a[i] for i in range(len(a)) if i not in [0,4,5]])
# print([x for i,x in enumerate(a) if i not in [0,4,5]])


# Question 86
# > **_By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]._**
# > **_Use list's remove method to delete a value._**
# a=[12,24,35,24,88,120,155]
# print(a)
# print(list(filter(lambda x:x!=24,a)))
# print([x for x in a if x!=24])
# a.remove(24)    #只删除第一个24
# print(a)


# Question 87
# > **_With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists._**
# > **_Use set() and "&=" to do set intersection operation._**
# a=[1,3,6,78,35,55]
# b=[12,24,35,24,88,120,155]
# print(set(a) & set(b))


# Question 88
# > **_With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved._**
# > **_Use set() to store a number of values without duplicate._**
# a=[12,24,35,24,88,120,155,88,120,155]
# #方法1
# b=[]
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)
# #方法2
# def RE(a):
#     dit={}
#     for x in a:
#         if x not in dit:
#             dit[x]=True
#             yield x
# print(list(RE(a)))


# Question 89
# > **_Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class._**
# > **_Use Subclass(Parentclass) to define a child class._**
class Person():
    def __init__(self):
        self.gender='Unknown'
    def getGender(self):
        print(self.gender)
class Male(Person):
    def __init__(self):
        self.gender='Male'
class Female(Person):
    def __init__(self):
        self.gender='Female'
a=Male()
b=Female()
c=Person()
a.getGender()
b.getGender()
c.getGender()
