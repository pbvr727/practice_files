#Number Reverse program
# n=int(input("Enter n number:"))#n=12345
# r=0
# while n>0:
#     digi=n%10
#     r=(r*10)+digi
#     n=n//10
# print(r)
# print(90//10)
# print(90%10)
# l1=[]
# for i in [1,23,22,4,55]:
#     print("list=",i//10)#0
#     print("list1div=",i%10)#
#     l1.append(i%10)
# print(l1)
#Python Program to Check Whether a Given Number is Even or Odd using Recursion
# def add(n):
#     if n>2:
#         return (n%2==0)
#     return add(n-2)
# print(add(11))
# n=int(input("Enter N number:"))
# t="positive Numbe" if n>0 else "Negaive number"
# print(t)
#Python Program to Check if a Number is a Palindrome
# n=int(input("Enter n number:"))
# temp=n
# r=0
# while 0<n:
#     d=n%10
#     r=(r*10)+d
#     n=n//10
# if temp==r:
#     print("Number is Plaindome:")
# else:
#     print("Number is not palindrome")
#Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

# n=int(input("enter n number:"))
# for i in range(1,100):
  
#     if i%n==0:
#         print("i=",i,i*5)
# #         # c=c+1
# n=8008887078
# n1=str(n)
# c=0
# for i in n1:
#     c=c+1
# print(c,"N numbers count:)")
# c=0
# while n>0:
#     n=n//10
#     c=c+1
# print(c)
# n=5
# while n>0:
#     print("ENTER N NUMBERE:")
#     n=n-1
# def fact(i):
#     if i==0:
#         return 1
#     else:
#         return i*fact(i-1)
# print(fact(10))
# a,b=0,1
# for i in range(1,109):
#     c=a+b
#     a,b=b,c
    # print(c)
# #Arm strong Number
# n=371
# t=n
# d1=0
# s1=len(str(n))
# for _ in range(s1):
#     d=t%10
#     d1=d1+d**s1
#     t=t//10
# if d1==n:
#     print("ARM SRONG NUMBER")
# else:
#     print("Not Arm")
# l=[]
# for i in range(2,100):
#     for j in range(2,int(i*0.5)+1):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(l)
# n=int(input("Enter n number:"))
# if n<2:
#     print("Hello")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("hello")
#             break
#     else:
#         print("Prime")
######String Manipulations###########
# s="aabcaabacddsssbbbbb"#2a1b1c1a1b1a1c2d
# s1=s[0];c=0;s2=""
# for i in s:
#     if i==s1:
#         c=c+1
#     else:
#         s2+=str(c)+s1
#         s1=i
#         c=1
# s2+=str(c)+s1
# print(s2)
s="Puvvada Bala Venkata Ramanjaneyulu"
# s1=""
# for i in range(len(s)):
#     s1=s[i]+s1
# print(s1)
# l1=[]
# for i in s.split():
#     print(i[::-1])
#     l1.append(i[::-1])
# print(l1)
# print(" ".join(l1))
import re 
# e=re.subn("a","@",s)
# print(e)
# e=re.finditer("[a,e,i,o,u]",s)
# c=0
# for i in e:
#     print(i.group())
#     c=c+1
# print(c)
# e=re.findall("a",s)
# print(e)
# e1=re.findall("[ba*]","bala venkata")
# print(e1)
#################################list##############3
l=[2,3,9,8,4,1,0,-19,1,4]
taget=5
l1=[]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]+l[j]==taget:
#             l1.append((l[i],l[j]))
# print(set(l1))

# def recur(l):
#     l1=[]
#     for i in l:
#         if  isinstance(i,list):
#             l1.extend(recur(i))
#         else:
#             l1.append(i)
#     return l1
# l=[1,2,[3,4,5],[6],9,78]
# print(recur(l))
# print(l)
# l=[1,2,3,1,2,3,4,5,7]
# l1=[i for i in range(len(l)) if l.count(i)==1]
# print(l1)
# n=6
# s=0
# for i in range(1,n):
#     if n%i==0:
#         print(i)
#         s=s+i
# print(s)
# if s==n:
#     print("Perfect Number")
# else:
#     print("Not Perfect")

# n=154
# t=0
# for i in range(1,n):
#     if n%i==0:
#         t=t+i
# print(t)
# if t==n:
#     print("Perfefct")
# else:
#     print("Not pefect")
# d={"a":[],"b":[]}
# for i in range(1,10):
#     if i%2==0:
#         d['a'].append(i)
#     else:
#         d['b'].append(i)
# print(d)
# l2=[]
# for x,y in zip(d['a'],d['b']):
#     l2.append(x**y)
# print(l2)
# with open("balaji.txt","a") as f1:
#     f1.write("Hello Everyone \n")
#     f1.write("If you want, I can also explain perfect number logic for interviews or optimize the code 👍 \n")

# l=[0,3,1,4,3,7,6,9,2]
# l1=l[0]
# l1=l[1]
# target=7
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l1>l2

# for i in "Ramanjaneyulu":
#     print(abs(ord(i)-(ord(i)-1)))

# s=[1,2,4]
# def bubble(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 l[i],l[j]=l[j],l[i]
#     return l
# l=[4,1,2,9,5,6,8,8]
# # print(bubble(l))
# c=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         l[i:j]
#         c=c+1
# print(c)
# d={"a":2,"b":3,"c":4,"d":3,"e":3,"k":1,"p":0}
# d1={}
# for k,v in enumerate(d):
#     print(k,":",v)
#     if v not in d1:
#         d1[v]=k
# print(d1)
# from collections import Counter
# d={"a":2,"b":3,"c":4,"d":3,"e":3,"k":1,"p":0}
# y=Counter(d)
# print(y)
# y1=Counter(l).most_common(2)
# print(y1)
# it='B4A1D3p9b7'#ot=BBBBADDD
# s1=""
# s2=""
# f=""
# for i in range(0,len(it),2):
#     f=it[i]
#     s2=s2+f*int(it[i+1])
# print(s2)
l=[1,2,3,"h"]
# if l is isinstance(l,(int,list)):
#     print(l)
for i in l:
    if isinstance(i,list):
        print(i)
print("//\//\\//\\//\\\/")
import  re
e=re.findall("ab?","rambabu ")
print(e)
s="Puvvada Bala Venkata Ramanjaneyulu"
l=[]
for i in range(len(s)):
    l.append(s[i])
print(l)
print("".join(l))


def decor(func):
    def inner(*args,**kwags):
        
        t=func(*args,**kwags)
        return t
    return inner
@decor
def simple(a,b):
    return a+b
print(simple(10,5))










    










        
    




