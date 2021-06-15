
#Question 10
'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''

# seq=sorted(list(set(input().split(' '))))
# print(' '.join(seq))


'''
#Question 11
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010

seq=input('请输入几个长度为4位的二进制数以逗号隔开：').split(',')
print(seq)
#方法1
def BinaryToTen(x):
    x=str(x)
    x_len=len(x)
    Ten=0
    for i in range(x_len):
        if x[i]=='1':
            Ten+=2**(x_len-i-1)
    if Ten%5==0:
        return x
    else:
        return

a=[bina for bina in seq if BinaryToTen(bina)]
print(','.join(a))

#方法2
lst=list(filter(lambda x:int(x,2)%5==0,seq))
print(','.join(lst))
'''
'''
#Question 12
#Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#方法1
lst=[]
for i in range(1000,3001):
    if i%2==0:
        i=str(i)
        flag=1
        for j in i:
            if int(j)%2!=0:
                flag=0
                break
        if flag==1:
            lst.append(i)
print(','.join(lst))

#方法2
def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element
lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))
#方法2.1
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))
'''

#Question 13
#
'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
#方法1
seq=input()
LETTERS=0
DIGITS=0
for i in seq:
    if i.isalpha():
        LETTERS+=1
    elif i.isdigit():
        DIGITS+=1
print('LETTERS %d'%LETTERS)
print('DIGITS %d'%DIGITS)

#方法2
import re
print('LETTERS %d'%(len(re.findall('[a-zA-Z]',seq))))
print('DIGITS %d'%(len(re.findall('[1-9]',seq))))
