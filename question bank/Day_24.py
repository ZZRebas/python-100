# Question 100
# > **_You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification._**
# > **_If the following string is given as input to the program:_**
# > 4
# bcdef
# abcdefg
# bcde
# bcdef
# > **_Then, the output of the program should be:_**
# > 3
# > 2 1 1
# > **_Make a list to get the input order and a dictionary to count the word frequency_**
# lst=[]
# while True:
#     l=input()
#     if not l:
#         break
#     lst.append(l)
# dit={}
# for i in lst:
#     dit[i]=dit.get(i,0)+1
# print(' '.join([str(i) for i in dit.values()]))


# Question 101
# > **_You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency._**
# > **_If the following string is given as input to the program:_**
# > aabbbccde
# > **_Then, the output of the program should be:_**
# > b 3
# > a 2
# > c 2
# > d 1
# > e 1
# > **_Count frequency with dictionary and sort by Value from dictionary Items_**
# st='aabbbccde'
# dict={}
# for i in st:
#     dict[i]=dict.get(i,0)+1
# res=sorted(dict.items(),key=lambda x:x[1],reverse=True)     #方法1
# # res=sorted(dict.items(),key=lambda x:(-x[1],x[0]))        #方法2
# print(res)
# for k,v in res:
#     print(k,v)
# #方法3
# s ='aabbbccde'
# dict_count_ = {k:s.count(k) for k in s}
# list_of_tuples = [(k,v) for k,v in dict_count_.items()]
# list_of_tuples.sort(key = lambda x: x[1], reverse = True)
# for item in list_of_tuples:
#     print(item[0], item[1])


# Question 102
# > **_Write a Python program that accepts a string and calculate the number of digits and letters._**
# **Input**
# > Hello321Bye360
# **Output**
# > Digit - 6
# > Letter - 8
# s='Hello321Bye360'
# Digit=0
# Letter=0
# for i in s:
#     Digit+=i.isdigit()
#     Letter+=i.isalpha()
# print(f'Digit - {Digit}')
# print(f'Letter - {Letter}')


# Question 103
# > **_Given a number N.Find Sum of 1 to N Using Recursion_**
# **Input**
# > 5
# **Output**
# > 15
# > **_Make a recursive function to get the sum_**
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
print(sum(5))
