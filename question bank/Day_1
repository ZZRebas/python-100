#Question 1
#Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# a=[str(i) for i in range(2000,3200) if i%7==0 and i%5!=0]
# print(','.join(a))
# print(list(filter(lambda x:x%7==0 and x%5!=0,range(2000,3200))))

'''
#Question 2：求一个数的阶乘
#方法1，递归
num=int(input('请输入一个整数：'))

def factorial(n):
    return 1 if n==1 else n*factorial(n-1)
res=factorial(num)
print('%d的阶乘为%d'%(num,res))

#方法2，for循环
fact=1
for i in range(1,num+1):
    fact*=i
print('%d的阶乘为%d'%(num,fact))

#方法3，高阶函数reduce
from functools import reduce
res=reduce(lambda x,y:x*y,range(1,num+1))
print('%d的阶乘为%d'%(num,res))
'''


#Question 3:
#With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#方法1，for循环
num=int(input('请输入一个整数：'))
dt={}
for i in range(1,num+1):
    dt[i]=i*i
print(dt)

#方法2，字典推导式（同列表推导式）
print({i:i*i for i in range(1,num+1)})

