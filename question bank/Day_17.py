# Question 65
# > **_Please write assert statements to verify that every number in the list [2,4,6,8] is even._**
# > **_Use "assert expression" to make assertion._**
# assert 断言，判断是否有错
# for i in [2,4,6,9]:
#     assert i%2==0 ,'%d is not even number'%i


# Question 66
# > **_Please write a program which accepts basic mathematic expression from console and print the evaluation result._**
# > **_Example:
# > If the following n is given as input to the program:_**
# 35 + 3
# > **_Then, the output of the program should be:_**
# 38
# print(eval(input()))


# Question 67
# > **_Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list._**
# > **_Use if/elif to deal with conditions._**
#TODO 二分查找法
# def search(n,lst):
#     left=0
#     right=len(lst)
#     while left<=right:
#         mid=(left+right)//2
#         if lst[mid]==n:
#             return mid
#         elif lst[mid]>n:
#             right=mid-1
#         elif lst[mid]<n:
#             left=mid+1
#     return None
# lst=[2,5,7,9,12,23,46,75,89,90]
# print(search(9,lst))    #3
# print(search(10,lst))   #None


# Question 68
# > **_Please generate a random float where the value is between 10 and 100 using Python module._**
# > **_Use random.random() to generate a random float in [0,1]._**
# import random
# print(random.uniform(10,100))


# Question 69
# > **_Please generate a random float where the value is between 5 and 95 using Python module._**
# > **_Use random.random() to generate a random float in [0,1]._**
import random
print(random.random()*100-5)
print(random.uniform(5,95))