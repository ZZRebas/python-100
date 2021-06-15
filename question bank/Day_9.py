# Question 26
# **_Define a function which can compute the sum of two numbers._**
#方法1
# def sum(x):
#     return int(x[0])+int(x[1])
# print(sum(input('输入两个数用空格隔开').split(' ')))

#方法2
# from functools import reduce
# print(reduce(lambda x,y:int(x)+int(y),input('输入多个数用空格隔开').split()))


# Question 27
# **_Define a function that can convert a integer into a string and print it in console._**
# def num_to_str(n):
#     n_str=str(n)
#     print(n_str)
#     print(type(n_str))
# num_to_str(5)


# Question 28
#**_Define a function that can receive two integer numbers in string form and compute their sum and then print it in console._**
# def sum(x):
#     return int(x[0])+int(x[1])
# print(sum(input().split()))


# Question 29
#**_Define a function that can accept two strings as input and concatenate them and then print it in console._**
# def conc(str1,str2):
#     return str1+str2
# print(conc('abc','def'))


# Question 30
#**_Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line._**
#方法1
def maximum(str1,str2):
    if len(str1)>len(str2):print(str1)
    elif len(str1)<len(str2):print(str2)
    else:
        print(str1+'\n'+str2)
maximum('abc','defg')

#方法2
func=lambda a,b:print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
func('one','three')

