# Question 20
# > **_Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n._**
# > **_Suppose the following input is supplied to the program:_**
# 14
# > **_Then, the output should be:_**
# 0
# 7
# 14

# class Gen_num():
#     def f(self,x):
#         for i in range(x+1):
#             if i%7==0:
#                 yield i
#
# generator=Gen_num().f(int(input()))
# for it in generator:
#     print(it)

#Question 21
# > **_A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:_**
# > **_The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer._**
# > **_Example:_**
# > **_If the following tuples are given as input to the program:_**
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# > **_Then, the output of the program should be:_**
# 2
import math
xy_dict={'x':0,'y':0}
while True:
    s=input()
    if not s:
        break
    toword=s.split(' ')[0]
    num=int(s.split(' ')[-1])
    if toword =='UP':
        xy_dict['y']+=num
    elif toword =='DOWN':
        xy_dict['y']-=num
    elif toword =='RIGHT':
        xy_dict['x']+=num
    elif toword =='LEFT':
        xy_dict['x']-=num
res=int(math.sqrt(xy_dict['x']**2+xy_dict['y']**2))
print(xy_dict['x'],xy_dict['y'])
print(res)
