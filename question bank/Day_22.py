# Question 90
# > **_Please write a program which count and print the numbers of each character in a string input by console._**
# > **_Example:
# > If the following string is given as input to the program:_**
# abcdefgabc
# > **_Then, the output of the program should be:_**
# ```
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
# > **_Use dict to store key/value pairs.
# > Use dict.get() method to lookup a key with default value._**
# def str_count(char):
#     dit={}
#     for c in char:
#         # dit[c]=char.count(c)  #方法1
#         dit[c]=dit.get(c,0)+1   #方法2
#     print(dit)
#     print('\n'.join(['%s %s'%(k,v) for k,v in dit.items()]))
# str_count('abcdefgabc')
# #方法3
# s='abcdefgabc'
# for i in sorted(set(s)):
#     print(f'{i} {s.count(i)}')


# Question 91
# > **_Please write a program which accepts a string from console and print it in reverse order._**
# > **Example:
# > If the following string is given as input to the program:\***
# rise to vote sir
# > **_Then, the output of the program should be:_**
# ris etov ot esir
# > **_Use list[::-1] to iterate a list in a reverse order._**
# s='rise to vote sir'
#方法1
# print(''.join(reversed(s)))
#方法2
# print(''.join(s[::-1]))



# Question 92
# > **_Please write a program which accepts a string from console and print the characters that have even indexes._**
# > **_Example:
# > If the following string is given as input to the program:_**
# H1e2l3l4o5w6o7r8l9d
# > **_Then, the output of the program should be:_**
# Helloworld
# s='H1e2l3l4o5w6o7r8l9d'
# print(''.join([s[i] for i in range(len(s)) if i%2==0]))
# print(s[::2])


# Question 93
# > **_Please write a program which prints all permutations of [1,2,3]_**
## Hints
# > **_Use itertools.permutations() to get permutations of list._**
# from itertools import permutations
# p=permutations([1,2,3])
# print(list(p))


# Question 94
# > **_Write a program to solve a classic ancient Chinese puzzle:
# > We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?_**
## Hints
# > **_Use for loop to iterate all possible solutions._**
hs=35
ls=94
def comput(hs,ls):
    '''
    hs=chickens+rabbits
    ls=chickens*2+rabbits*4
    0<= chickens <=35
    0<= rabbits <=94//4
    '''
    for ch in range(hs+1):
        ra=hs-ch
        if (ch*2+ra*4) == 94 and ra< (ls//4):
            print(f'chickens:{ch}')
            print(f'rabbits:{ra}')
comput(hs,ls)



