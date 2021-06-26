# Question 75
# > **_Please write a program to randomly print a integer number between 7 and 15 inclusive._**
# > **_Use random.randrange() to a random integer in a given range._**
# import random
# print(random.randint(7,15))
# print(random.randrange(7,16))


# Question 76
# > **_Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"._**
# > **_Use zlib.compress() and zlib.decompress() to compress and decompress a string._**
# import zlib
# str='hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
# str_bytes=bytes(str,'utf-8')
# str_com=zlib.compress(str_bytes)    #压缩字节类型数据
# print(str_com)
# print(zlib.decompress(str_com))     #解压缩


# Question 77
# > **_Please write a program to print the running time of execution of "1+1" for 100 times._**
# > **_Use timeit() function to measure the running time._**
# import time
# start=time.time()
# for i in range(100):
#     a=1+1
# end=time.time()
# print(start,end)
# print(end-start)


# Question 78
# > **_Please write a program to shuffle and print the list [3,6,7,8]._**
# > **_Use shuffle() function to shuffle a list._**
# import random
# a=[3,6,7,8]
# random.shuffle(a)
# print(a)


# Question 79
# > **_Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]._**
# > **_Use list[index] notation to get a element from a list._**
#方法1
subject=["I", "You"]
verb=["Play", "Love"]
object=["Hockey","Football"]
print('\n'.join(['%s %s %s'%(i,j,k) for i in subject for j in verb for k in object]))
# #方法2
import itertools
sentence = [subject, verb, object]
n = list(itertools.product(*sentence))
for i in n:
    print(i)

from itertools import product
for i,j in product([1,2,3],[4,5]):      #product()相当于嵌套的for
    print(i,j)
