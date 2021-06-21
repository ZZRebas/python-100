# Question 54
# > **_Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only._**
# > **_Example:
# > If the following email address is given as input to the program:_**
# john@google.com
# > **_Then, the output of the program should be:_**
# google
import re
# email="john@google.com"
# pat="^[a-zA-Z]+@([a-z]+)\.com"
# print(re.findall(pat,email))


# Question 55
# > **_Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only._**
# > **_Example:
# > If the following words is given as input to the program:_**
# 2 cats and 3 dogs.
# > **_Then, the output of the program should be:_**
# ['2', '3']

# pat="(\d+)\s|\s(\d+)$"
# seq='2 cats and 3 dogs 3sd 2323'
# print(re.findall(pat,seq))


# Question 56
# > **_Print a unicode string "hello world"._**
# > **_Use u'strings' format to define unicode string._**
# unicodeString=u'hello world!'
# print(unicodeString)


# Question 57
# > **_Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8._**
# > **_Use unicode()/encode() function to convert._**
# s=input()
# u=s.encode('utf-8')
# print(u)


# Question 58
# > **_Write a special comment to indicate a Python source code file is in unicode._**
# > **_Use unicode() function to convert._**

# -*- coding:utf-8 -*-


# Question 59
# > **_Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)._**
# > **_Example:
# > If the following n is given as input to the program:_**```
# 5
# > **_Then, the output of the program should be:_**
# 3.55

def f(n):
    if n==1:
        return 1/2
    return n/(n+1) + f(n-1)
print('%.2f'%f(int(input())))


