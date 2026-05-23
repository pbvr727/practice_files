
# c=1
# def rec():
#     global c
#     if c<=10:
#         print("Bala Venkata Ramanjaneyulu")
#         c=c+1
#         rec()
# # print(rec())
# def rec(l,sart=0,end=None):
#     if end in None:
#         print(l[sart]:[end])
# l=[0,1,2,3,4,5]
# print(rec(l,sart=0,end=6))
# a=eval(input("enter a number"))
# print(type(a))
# def add(l,start,end):
#     if start>=end:
#         return
#     else:
#         print(l[start:end])
#         add(l,start+1,end)
#     return l[start:end]
# print(add(l=[10,20,30,40,50],start=0,end=0))
#Menu Driven program

# while True:
#     first=int(input("enter first number:"))
#     second=int(input("enter second number:"))
#     print("1.addition \n 2.sub \n 3.mul")
#     type=int("enter num here:")

#     if type==1:
#         print(first+second)
#     elif type==2:
#         print(first-second)
#     elif type==3:
#         print(first*second)
#     else:
#         print("There is No NUmber:")
# s="puvvada"
# l=[]
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         l.append(s[i:j])
# print(l)
# c=1
# for i in range(5,0,-1):
#     c=c*i
#     print(c)
# import sys
# num=22
# print(sys.getsizeof(num))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)
# print(sys.getsizeof(num))
# l=["Balaji","Puvvada",121]
# for i in l:
#     l.append(i)  
# print(l)
# i=0
# while i<=2:
#     print("Balaji")
#     j=1
#     while j<=2:
#         print("Hello inner")
#         j=+1
#     i=+1

# d={}
# l=[]
# query="a=2&b=23&name=prakash"
# for i in query.split("&"):
#     l.append(i.split("="))
# print(dict(l))
# s = "vInEeTkAsHyAp"
# s1=""
# for i in range(0,len(s),2):
#     s1=s1+s[i].upper()
# print(s1)
# for i in range(1,20):
#     for k in range(1,9):
#         print(" ",end="")
#         for j in range(8,10):
#             print("*",end=" ")

#     print()
from collections import Counter
s="puvvada bala venkata ramanjaneyulu"
# d=re.compile("a",s)
# for i in d:
#     print(i.start())
d=Counter(s)
print(d)
l=[10,0,3,2,2,4,9,11]
for i in range(len(l)):
    for j in range(i,len(l)-1):
        if l[i]>l[j+1]:
            l[i],l[j+1]=l[j+1],l[i]
print(l[-2])
n=153
temp=n
r=0
while 0<n:
    d=n%10
    r=r+d**3
    n=n//10
print(r)
if temp==r:
    print("Number palindrome")
else:
    print("not palindrome",r)
    ######################
def add(l,s,e):
    if s>e:
        return
    else:
        #print(l[s:e])
        add(l,s+1,e)
    return l[s:e]
# l=[10,20,30,40,50]
# s=3
# e=len(l)+1

# print(add(l,s,e))
s=123456789
r=0
while 0<s:
    d=s%10
    r=r*10+d
    s=s//10
print(r)

