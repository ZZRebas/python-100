'''
#Question 16
# > **_Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers._** >**_Suppose the following input is supplied to the program:_**
# 1,2,3,4,5,6,7,8,9
# > **_Then, the output should be:_**
# 1,9,25,49,81

num_list=input().split(',')
res=[str(int(i)**2) for i in list(filter(lambda x:int(x)%2!=0,num_list))]
print(','.join(res))
lst=[str(int(i)**2) for i in num_list if int(i)%2]
print(','.join(lst))
'''


#Question 17
# > **_Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:_**
# D 100
# W 200
# - D means deposit while W means withdrawal.
# > **_Suppose the following input is supplied to the program:_**
# D 300
# D 300
# W 200
# D 100
# > **_Then, the output should be:_**
# 500

amount=0
while True:
    s=input('请输入存款D或者取款W和金额,用空格隔开')
    if not s:
        break
    DW=s.split(' ')[0]
    num=s.split(' ')[-1]
    if DW=='D':
        amount+=int(num)
    elif DW=='W':
        amount-=int(num)
print('账户余额为%d'%amount)


