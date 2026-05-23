# try:
# except ZeroDivisionError as d:
#     print(d)
# except TypeError as t:
#     print(t)
# # else:
# #     print("else block")
# finally:
#     print("succesdsfuullly")

# v=10
# try:
#     if not hasattr(v,"__iter__"):
#         raise TypeError
#     for p in v:
#         print(p)
# except TypeError:
#     print("Hello")
s="Puvvada Bala venkata Ramanjaneyuluu"
i=0
s1=""
# for i in s:
#     s1=i+s1
# print(s1)
while i<len(s):
    s1=s[i]+s1
    i+=1
print(s1)
l1=[]
for i in s.split():
    r=i[::-1]
    l1.append(r)
print(" ".join(l1))
l=[1,2,3,45,6,7,8,10,98]
l1=l[0]
# for i in range(len(l)-1,0,-1):
#     l1.append(l[i])
# print(l1)
# for i in range(1,len(l),2):
#     print(l[i])
# print(l[-2::])
# for i in range(len(l)):
#     for j in range(i,len(l)-1):
#         if l[i]<l[j+1]:
#             l[i],l[j+1]=l[j+1],l[i]
# print(l)
for i in range(len(l)):
    if l[i]>l1:
        l1=l[i]
print(l1)
d={"A":10,"B":100}
for i,k in d.items():
    print(i,":",k)
print(d.popitem())
print(d)
import re
c=0
s="puvvada bala venkata ramanjaneyulu bpuvvada3@gmail.com, sdnakj balaji@yahoo.com, omkar siva@outlook.com"
# m=re.finditer("\W",s)
# for i in m:
#     print(i.start(),"Start",i.end(),"end",i.group())
#     c=c+1
# print(
r1=re.split(" ",s)
print(r1)
print(re.fullmatch("\W[a-zA-Z0-9]@[a-z][.]com]",s))
# q="a4b3c2a1"
# y=""
# y1=""
# y2=""
# for i in q:
#     if i.isalpha():
#         y=i
#     else:
#         y1=y*int(i)
#         y2=y2+y1

# print(y2)
# q="aaabbcceeettt"
# r=q[0]
# c=0
# p=""
# for i in q:
#     if i==r:
#         c=c+1
#         # print(c)
#     else:
      
       
#        p=p+r+str(c)
#        r=i
#        c=1  
      
# print(p)
# d="balaji venkata"
# d1={}
# for i in d:
#     if i in d1:
#         d1[i]=d1[i]+1
#     else:
#         d1[i]=1
# print(d1)
# s=int(input("enter s value:"))
# print(s)
# n=int(input("enter value:"))
# for i in range(n):
#     print(i)
n=int(input("enter n number:"))
r=0
while 0<n:
    d=n%10
    r=r+d**3
    n=n//10
print(r)
import datetime

def decor(func):
    def inner(a,b):
        st=datetime.datetime.now()
        result=func(a,b)
        end=datetime.datetime.now()
        d=end-st
        print(d)
        return result
    return inner
@decor
def add(a,b):
    print(a+b)
add(52,10)


