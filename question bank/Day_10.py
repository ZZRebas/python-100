# Question 31
# > **_Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys._**
# ### Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.
#方法1
# def squre_dict():
#     dict_1={}
#     for i in range(1,21):
#         dict_1[i]=i**2
#     return dict_1
# print(squre_dict())
#方法2
# def sq_dict():
#     dict_2={i:i**2 for i in range(1,21)}
#     return dict_2
# print(sq_dict())


# Question 32

### **Question:**
# > **_Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only._**
# ### Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
# def squre_dict():
#     dict_1={}
#     for i in range(1,21):
#         dict_1[i]=i**2
#     for k in dict_1.keys():
#         print(k)
# squre_dict()
#
# def sq_dict():
#     d={i:i**2 for i in range(1,21)}
#     print(d.keys())
# sq_dict()


# Question 33
# > **_Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included)._**
### Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.
# print([i**2 for i in range(1,21)])


# Question 34
#_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list._**
# print([i**2 for i in range(1,21)][:5])


# Question 35
#_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list._**
# print([i**2 for i in range(1,21)][-5:])


# Question 36
#_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list._**
# print([i**2 for i in range(1,21)][5:])


# Question 37
#_Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)._**
# print(tuple([i**2 for i in range(1,21)]))
# print(tuple(i**2 for i in range(1,21)))


