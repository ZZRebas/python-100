# Question 95
# > **_Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up._**
# > **_If the following string is given as input to the program:_**
# > 5
# > 2 3 6 6 5
# > **_Then, the output of the program should be:_**``
# > 5
# a=[2,3,6,6,5]
# #方法1
# c=sorted(set(a))
# print(c[-2])
# #方法2
# b=[(max(a)-a[i],i) for i in range(len(a)) if max(a)-a[i] != 0 ]
# b.sort()
# print(a[b[0][1]])


# Question 96
# > **_You are given a string S and width W.
# > Your task is to wrap the string into a paragraph of width._*
# > **_If the following string is given as input to the program:_**
# > ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 4
# > **_Then, the output of the program should be:_**
# > ABCD
# > EFGH
# > IJKL
# > IMNO
# > QRST
# > UVWX
# > YZ
# n=4
# st=input()
# #方法1
# for i in range(1,len(st)):
#     print(st[i-1],end='')
#     if i%n==0 :
#         print()
#     if i==len(st)-1:
#         print(st[i])
# #方法2
# import textwrap
# print(textwrap.fill(st,width=n))
# print('\n'.join(textwrap.wrap(st,width=n)))


# Question 97
# > **_You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)_**
# > **_Different sizes of alphabet rangoli are shown below:_**
# > #size 3
# > ----c----
# > --c-b-c--
# > c-b-a-b-c
# > --c-b-c--
# > ----c----
# > #size 5
# > --------e--------
# > ------e-d-e------
# > ----e-d-c-d-e----
# > --e-d-c-b-c-d-e--
# > e-d-c-b-a-b-c-d-e
# > --e-d-c-b-c-d-e--
# > ----e-d-c-d-e----
# > ------e-d-e------
# > --------e--------
#方法1
import string
alphabet=string.ascii_lowercase
input_letter=input()
letter_item=alphabet.index(input_letter)
#n与每行长度的规律：4n+1
down=[]
for row in range(letter_item+1):
    right=alphabet[letter_item-row:letter_item+1]
    rights='-'.join(right)
    lefts='-'.join(right[:0:-1])
    rl=lefts+'-'+rights
    if row==0:
        rl=lefts+rights
    down.append(rl.center(4*letter_item+1,'-'))
    print(rl.center(4*letter_item+1,'-'))
print('\n'.join(down[len(down)-2::-1]))
#方法2
def rangoli(n):
    l1=list(map(chr,range(97,123)))
    x=l1[n-1::-1]+l1[1:n]
    mid=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-'))
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-'))
rangoli(5)


# Question 98
# > **_You are given a date. Your task is to find what the day is on that date._**
# **Input**
# > **_A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format._**
# > 08 05 2015
# **Output**
# > **_Output the correct day in capital letters._**
# > WEDNESDAY
# > **_Use weekday function of calender module_**
# import calendar
# month, day, year = map(int, input().split())
# dayId = calendar.weekday(year, month, day)
# print(calendar.day_name[dayId].upper())


# Question 99
# > **_Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both._**
# **Input**
# > **_The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers._**
# > 4
# > 2 4 5 9
# > 4
# > 2 4 11 12
# **Output*
# > **_Output the symmetric difference integers in ascending order, one per line._**
# > 5
# > 9
# > 11
# > 12
#TODO 对称差=并集-交集 or 异或运行

# a=set(map(int,input().split()))
# b=set(map(int,input().split()))
# 方法1
# print('\n'.join([str(i) for i in list(a^b)]))
#方法2
# c=(a | b) - (a & b)
# print('\n'.join([str(i) for i in sorted(c)]))

