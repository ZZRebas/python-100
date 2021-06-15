#Question 18
# > **_A website requires the users to input username and password to register. Write a program to check the validity of password input by users._**
# > **_Following are the criteria for checking the password:_**
# - **_At least 1 letter between [a-z]_**
# - **_At least 1 number between [0-9]_**
# - **_At least 1 letter between [A-Z]_**
# - **_At least 1 character from [$#@]_**
# - **_Minimum length of transaction password: 6_**
# - **_Maximum length of transaction password: 12_**
# > **_Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma._**
#  > **_Example_**
# > **_If the following passwords are given as input to the program:
# _** ABd1234@1,a F1#,2w3E*,2We3345
#  **_Then, the output of the program should be:\
# _**ABd1234@1

#错误方法
# import re
# str_lst=input().split(',')
# for st in str_lst:
#     if len(st)>=6 and len(st)<=12:
#         # pattern=re.compile(r'(.*\d+)(.*[a-z]+)(.*[A-Z]+)(.*[$#@]+)')
#         pattern=re.compile(r'.*\d+.*[a-z]+.*[A-Z]+.*[$#@]+')
#         m=pattern.search(st)
#         if m:
#             print(st)

#方法1
# a = input('Enter passwords: ').split(',')
# pass_pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
# for i in a:
#     if pass_pattern.fullmatch(i):
#         print(i)

#方法2
import re
value = []
items = [x for x in input().split(',')]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print( ",".join(value))

#方法3
s = input().split(',')
lst = []
for i in s:
    cnt = 0
    cnt+=(6<=len(i) and len(i)<=12)
    cnt+=bool(re.search("[a-z]",i))      # here re module includes a function re.search() which returns the object information
    cnt+=bool(re.search("[A-Z]",i))      # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
    cnt+=bool(re.search("[0-9]",i))      # if not a single match found then returns NONE which converts to False in boolean
    cnt+=bool(re.search("[@#$]",i))      # expression otherwise True if found any.
    if cnt == 5:
        lst.append(i)

print(",".join(lst))


#Question 19
# > **_You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:_**
# - **_1: Sort based on name_**
# - **_2: Then sort based on age_**
# - **_3: Then sort by score_**
# > **_The priority is that name > age > score._**
# > **_If the following tuples are given as input to the program:_**
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# > **_Then, the output of the program should be:_**
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# all_lst=[]
# while True:
#     exp=input()
#     if not exp:
#         break
#     exp=tuple(exp.split(','))
#     all_lst.append(exp)
# print(all_lst)
# all_lst.sort(key=lambda x:(x[0],int(x[1]),int(x[2])))
# print(all_lst)
#
