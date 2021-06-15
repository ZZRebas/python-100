'''
#Question 14
#> **_Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters._**
# > **_Suppose the following input is supplied to the program:_**
# Hello world!
# > **_Then, the output should be:_**
# UPPER CASE 1
# LOWER CASE 9
#方法1
import re
st=input()
print('LOWER CASE',len(re.findall('[a-z]',st)))
print('UPPER CASE',len(re.findall('[A-Z]',st)))

#方法2
word = input()
upper,lower = 0,0
for i in word:
    lower+=i.islower()
    upper+=i.isupper()
print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
'''


#Question 15
# > **_Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a._**
# > **_Suppose the following input is supplied to the program:_**
# 9
# > **_Then, the output should be:_*
# 11106

num=input()
print(eval('%s+%s%s+%s%s%s+%s%s%s%s'%(num,num,num,num,num,num,num,num,num,num)))
print(int(num)+int(num*2)+int(num*3)+int(num*4))
print(sum(int(num * i) for i in range(1,5)))
from functools import reduce
print(reduce(lambda x,y:int(x)+int(y),[num * i for i in range(1,5)]))
