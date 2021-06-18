# Question 38
#_With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line._**
#> **_Use [n1:n2] notation to get a slice from a tuple._**
# tup=(1,2,3,4,5,6,7,8,9,10)
# print(tup[:5])
# print(tup[5:])


# Question 39
# > **_Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)._**
# > **_Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list._**
# tup=(1,2,3,4,5,6,7,8,9,10)
# print(tuple(i for i in tup if i%2==0))
# print(tuple(filter(lambda x:x%2==0,tup)))


# Question 40
# > **_Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No"._**
# > **_Use if statement to judge condition._**
# st=input()
# if st in ['YES','yes','Yes']:
#     print('Yes')
# else:
#     print('No')
# print(''.join(['Yes' if st in ['YES','yes','Yes'] else 'No']))


# Question 41
# > **_Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]._**
# > **_Use map() to generate a list.Use lambda to define anonymous functions._**
# lst=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,lst)))


# Question 42
# > **_Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]._**
# > **_Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions._**
#方法1
# lst=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,lst)))))
#方法2
# def even(x):
#     return x%2==0
# def squer(x):
#     return x*x
# print(list(map(squer,filter(even,lst))))


# Question 43
# > **_Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)._**
# > **_Use filter() to filter elements of a list.Use lambda to define anonymous functions._**
print(list(filter(lambda x:x%2==0,range(1,21))))




