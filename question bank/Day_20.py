# Question 80
# > **_Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24]._**
# > **_Use list comprehension to delete a bunch of element from a list._**
# a=[5,6,77,45,22,12,24]
# print(list(filter(lambda x:x%2!=0,a)))
# print([x for x in a if x%2!=0])


# Question 81
# > **_By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]._**
# > **_Use list comprehension to delete a bunch of element from a list._**
# a=[12,24,35,70,88,120,155]
# print([x for x in a if x%35!=0])


# Question 82
# > **_By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]._**
# > **_Use list comprehension to delete a bunch of element from a list.
# > Use enumerate() to get (index, value) tuple._**
# a=[12,24,35,70,88,120,155]
# print([x for i,x in enumerate(a) if i not in [0,2,4,6]])
# print([a[i] for i in range(len(a)) if i%2!=0])


# Question 83
# > **_By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155]._**
# > **_Use list comprehension to delete a bunch of element from a list.
# > Use enumerate() to get (index, value) tuple._**
# a=[12,24,35,70,88,120,155]
# print([x for i,x in enumerate(a) if i not in range(2,5)])
# print([a[i] for i in range(len(a)) if i not in range(2,5)])
# print([i for i in a if a.index(i) not in range(2,5)])


# Question 84
# > **_By using list comprehension, please write a program generate a 3\*5\*8 3D array whose each element is 0._**
# > **_Use list comprehension to make an array._**
print([[[0 for i in range(8)] for j in range(5)] for k in range(3)])
import numpy
print(numpy.zeros(shape=(3,5,8)))
