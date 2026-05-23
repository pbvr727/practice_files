#Flat list
# def rec(l):
#     l1=[]
#     for i in l:
#         if isinstance(i,list):
#             l1.extend(rec(i))
#         else:
#             l1.append(i)
#     return l1
# l=[[1,2,3],[4,5],[54],[],[6,[7,8]],9]
# # l=[[1,2,3],[4,5],[6,7]]
# print(rec(l))
#2)Non Repeated elemnts usinf functions
# def simple1(lst):
#     l3=[]
#     for i in lst:
#         if lst.count(i)==1:
#             l3.append(i)
#     return l3
# lst=[3,2,3,4,5,2,5,6,7]
# print(simple1(lst))
# #Using List Comprehension
# lst=[3,2,3,4,5,2,5,6,7]
# print([i for i in lst if lst.count(i)==1])
#Bubble sort
# def Bubble(l):
#     for i in range(len(l)):
#         for j in range(i,len(l)-1):
#             if l[i]>l[j+1]:
#                 l[i],l[j+1]=l[j+1],l[i]
#     return l
# l=[5,3,8,6,7,2,-2,2]
# print(Bubble(l))
########Reverse Integer##############
# num=123
# r=0
# while 0<num:
#     n=num%10
#     r=r*10+n
#     num=num//10
# print(r)
##############Without using 3rd number##############################
# a=10
# b=20
#Ariheaic Addition and subsracion
# a=a+b#10+20=30
# b=a-b#30-20=10
# a=a-b#30-10=20
# print(b,a)
#Biwise Operation
# a=a^b#10+20=30
# b=a^b#30-20=10
# a=a^b#30-10=20
# print(b,a)
##SUM SPLIT LIST--------------------------------
# #How many combination in list
l=[1,2,3,4,5,6,7,8,9,1]
# c=0
# for i in range(len(l)):
#     for j in range(1,len(l)):
#         l[i:j]
#         c=c+1
# print(c)
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==10:
            print((l[i],l[j]))       
print(l1)
######################################
#first 10 fibanocis series
# a=0;b=1
# for i in range(11):
#     c=a+b
#     a=b;b=c
#     print(c)
#################################
#factorial of number
# def fact(n):
#     if n<=1:
#         return 0
#     else:
#         return n+fact(n-1) 
# print(fact(5))
####################333333333333333333
#first n prime numbers
# l1=[]
# for i in range(2,n:=int(input("enter n number"))):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         l1.append(i)
# print(l1)
#####################################################
#find key index value
d={"a":2,"b":3,"c":4,"d":3,"e":3,"k":1,"p":0}
d1={}
l1=[]
for k,v in enumerate(d):
    print(k,v)
    if v not in d1:
        d1[v]=[k]
    else:
        d1[v].append(k)
print(d1)
print(l1)



