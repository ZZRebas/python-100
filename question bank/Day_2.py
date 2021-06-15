#Question 4:
#Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
# nums=input('输入一串数字，用逗号隔开：')
# num_list=nums.split(',')
# print(num_list)
# print(tuple(num_list))

'''
#Question 5:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class Getstr():
    def __init__(self):
        #python3可省略这个init初始化构造方法
        self.name=''
        self.age=''
        self.sex=''
    @classmethod    #使用了类方法@classmethod的函数，不用实例化，直接类名.方法名()调用
    def get_str(self):
        # self.characteristic=characteristic
        [self.name,self.age,self.sex]=input('请输入你的名字，年龄和性别，用逗号隔开：').split(',')
    @classmethod
    def print_str(self):
        print(('name:%s，age:%s，sex:%s。'
              %(self.name,self.age,self.sex)).upper())

Getstr.get_str()
Getstr.print_str()
'''


'''
#Question 6:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.

import math
C,H=50,30
def sqrt_(x):
    return int(math.sqrt(2*50*x/30))
num_list=input('输入一串数字用逗号隔开：').split(',')
print(','.join(list(map(lambda x:str(sqrt_(int(x))),num_list))))
# print(','.join(list(map(lambda x:str(int(math.sqrt(2*50*int(x)/30))),input('输入一串数字用逗号隔开：').split(',')))))
'''

'''
#Question 7:
#Write a program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array. The element value in the i-th row and j-th column
# of the array should be i _ j.*
#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x,y=map(int,input('输入两个数用逗号隔开：').split(','))
#方法1
import numpy as np
arr=np.zeros((x,y))
arr_shape=arr.shape
for i in range(arr_shape[0]):
    for j in range(arr_shape[1]):
        arr[i][j]=i*j
print(arr.astype(int).tolist())

#方法2
lst=[]
for i in range(x):
    inst=[]
    for j in range(y):
        inst.append(i*j)
    lst.append(inst)
print(lst)

#方法3
lst=[[i*j for i in range(y)] for j in range(x)]
print(lst)
'''

'''
#Question 8:
#Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

word_list=input('输入几个单词用逗号隔开：').split(',')
print(','.join(sorted(word_list)))

def my_func(e):
    return e[0]
my_list = input('Enter a comma separated string: ').split(",")
my_list.sort(key=my_func)
print(",".join(my_list))
'''

'''
#Question 9:
#Write a program that accepts sequence of lines as input and prints the lines
#after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

#方法1
# lines=[]
# while True:
#     line=input()
#     if line:
#         lines.append(line)
#     else:
#         break
# for line in lines:
#     print(line.upper())

#方法2
def inputs():
    while True:
        line=input()
        if not line:
            return
        yield line
print(*(line.upper() for line in inputs()),sep='\n')
# for line in map(str,inputs()):
#     print(line.upper())
'''
