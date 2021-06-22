# Question 60
# > **_Write a program to compute:_**
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# > **_with a given n input by console (n>0)._**
# > **_Example:
# > If the following n is given as input to the program:_**
# 5
# > **_Then, the output of the program should be:_**
# 500
#方法1
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n-1)+100
# print(f(int(input())))
# #方法2
# ff=lambda x:f(x-1)+100 if x>0 else 0
# print(ff(5))


# Question 61
# > **_The Fibonacci Sequence is computed based on the following formula:_**
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# > **_Please write a program to compute the value of f(n) with a given n input by console._**
# > **_Example:
# > If the following n is given as input to the program:_**
# 7
# > **_Then, the output of the program should be:_**
# 13
#方法1
# def Fibo(n):
#     if n==1 :
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return Fibo(n-1)+Fibo(n-2)
# print(Fibo(7))
#
# #方法2
# F=lambda x:0 if x==0 else 1 if x==1 else F(x-1)+F(x-2)
# print(F(7))


# Question 62
# > **_The Fibonacci Sequence is computed based on the following formula:_**
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# > **_Please write a program to compute the value of f(n) with a given n input by console._**
# > **_Example:
# > If the following n is given as input to the program:_**
# 7
# > **_Then, the output of the program should be:_**
# 0,1,1,2,3,5,8,13
#方法1
# def Fobi(n):
#     if n<2:
#         return n
#     else:
#         return Fobi(n-1)+Fobi(n-2)
# print(','.join(list(map(lambda x:str(Fobi(x)),range(7+1)))))
# print(','.join([str(Fobi(x)) for x in range(7+1)]))

#方法2
# def ff(n):
#     if n==0:
#         return [0]
#     elif n==1:
#         return [0,1]
#     seq=['0','1']
#     a,b,c=0,1,1
#     for i in range(2,n+1):
#         a=b
#         b=c
#         c=a+b
#         seq.append(str(b))
#     return seq
# print(','.join(ff(7)))


# Question 63
# > **_Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console._**
# > **_Example:
# > If the following n is given as input to the program:_**
# 10
# > **_Then, the output of the program should be:_**
# 0,2,4,6,8,10

# def gen(n):
#     for i in range(n+1):
#         if i%2==0:
#             yield i
# print(','.join([str(i) for i in gen(10)]))


# Question 64
# > **_Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console._**
# > **_Example:
# > If the following n is given as input to the program:_**
# 100
# > **_Then, the output of the program should be:_**
# 0,35,70

def f(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
print(','.join([str(i) for i in f(100)]))

