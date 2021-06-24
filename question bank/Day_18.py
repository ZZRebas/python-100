# Question 70
# > **_Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension._**
# > **_Use random.choice() to a random element from a list._**
# import random
# print(random.choice([x for x in range(11) if x%2==0]))


# Question 71
# > **_Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension._**
# > **_Use random.choice() to a random element from a list._**
# import random
# print(random.choice([i for i in range(10,151) if i %35==0]))


# Question 72
# > **_Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive._**
# > **_Use random.sample() to generate a list of random values._**
# import random
# import numpy.random
# print(random.sample(range(100,201),5))
# print(numpy.random.choice(range(100,201),5,replace=False))


# Question 73
# > **_Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive._**
# > **_Use random.sample() to generate a list of random values._**
# import random
# print(random.sample(range(100,201,2),5))
# print(random.sample([i for i in range(100,201) if i%2==0],5))


# Question 74
# > **_Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive._**
# > **_Use random.sample() to generate a list of random values._**
import random
print(random.sample([i for i in range(1,1001) if i%35==0],5))
