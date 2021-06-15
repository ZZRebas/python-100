#Question 22
# > **_Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically._**
#
# > **_Suppose the following input is supplied to the program:_**
#
# ```
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# ```
#
# > **_Then, the output should be:_**
#
# ```
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

#方法1
# seq_lst=input().split(' ')
# word_lst=sorted(seq_lst)
# seq_dict={}
# for seq in word_lst:
#     num=word_lst.count(seq)
#     seq_dict[seq]=num
# # print(seq_dict)
# for key in seq_dict:
#     print(key,':',seq_dict[key])

#方法2
# word_lst=input().split(' ')
# word_dict={i:word_lst.count(i) for i in word_lst}
# word_dict=sorted(word_dict.items())     #items() function returns both key & value of dictionary as a list
# for i in word_dict:
#     print('%s:%d'%(i[0],i[1]))

#方法3
# from collections import Counter
# ss = input().split()
# ss = Counter(ss)         # returns key & frequency as a dictionary
# print(ss)
# ss = sorted(ss.items())  # returns as a tuple list
# for i in ss:
#     print("%s:%d"%(i[0],i[1]))

#方法4
# from pprint import pprint
# p=input().split()
# pprint({i:p.count(i) for i in p})


# Question 23
# **_Write a method which can calculate square value of number_**
# def squ(x):
#     return x**2
# print(squ(int(input())))


# Question 24
# > **_Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions._**
#
# > **_Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()_**
#
# > **_And add document for your own function_**
#
# ### Hints:
#
# ```
# The built-in document method is __doc__

# print(str.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def sqrt(x):
#     '''return the square value of the number.
#     The input number must be integer'''
#     return x**2
# print(sqrt.__doc__)

class Student():
    classmate='A'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def p(self):
        print('%s %d %s'%(self.name,self.age,self.sex))
a=Student('Tom',18,'man')
a.p()
print(a.classmate)
print(Student.classmate,a.name)
a.name='Joe'
print(a.name)
a.p()

class Car:
    name = "Car"
    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))
toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))
