# # s="puvvada Bala Venkata Ramanjaneyulu"
# # print(s[-33:-30])
# s="\"""HI How ARE YOU \"I AM \"PYtHON\" Develope\'r since\" \n 2019 form till now\""""
# print(s)
# print("/\\/\\/\\/\\/\\/\\")
print("/\"")
# data=2E3
# print(type(data))
# print(data)
# print(ord('B'))
# print(ord('a'))
# print()
# c=0
# for i in "Balaji":
 
#     c=c+ord(i)
#     # print(ord(i))
#     print(c)
# # d="Balaji" if False else "Rama"
# # print(d)
# # print(a:=10)
# # for i in range(1,n:=int(input("enter n number:"))):
# #     print(i)
# # def simple(x,y):
# #     return f"{x},,,,,{y}"
# # print("Bahubali")
# # print(simple(10,11))
# i=0
# while (i:=i+1)<len(s:="puvvada"):
#     print("s",s)
s="Puvvada Bala Venkata Ramanjaneyulu"
# for i in s.split():
#     print(i)
# d={"a":10,"b":20}
# import sys
# l=[1,2,3,4,5,6]
# t=1,2,3,4,5,6
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))
# print(sys.getsizeof(d))
# l=[]
# for i in range(len(d:=s.split())-1,-1,-1):
#     print(d[i])
#     l.append(d[i])
# print(" ".join(l))
# l=[1,1,2,3,4,4,5,66,66]


# l1=[i for i in l if l.count(i)==1]
# print(l1)
#Find min and max values
# l=[45,78,12,46,98,66,53,21,63,87,89,91]
# l1=l[0]
# for i in l:
#     if i>l1:
#         l1=i
# print(l1)
# l=["simha","singham","sin1"]
# l.extend([1,2,3,4,56])
# print(l)
l=[10,9,3,6,4,6,8,12,14,15]
# l1=[i**2 for i in l if i%4==0] #if i%3==0] 
# print(l1)
# l2=[i*2 if i%2==0 else i for i in l]
# print(l2)

print(l1:=[i*3 if i%2==0 else i*2 for i in l])
# n=int(input("enter n number:"))


# for i in range(n):
#     for j in range(n):
#         print(i,j,end=" ")
#     print()
# print(a:=15)

print(u:=[l[i:j] for i in range(len(l)) for j in range(i+1,len(l)+1) if len(l[i:j])>=4])

# for i in range(len(l)):
#     for j in range(i+1,len(l)-i-1): 
#         if l[i]>l[j+1]:
#             l[i],l[j+1]=l[j+1],l[i]
# print(l)
print([(l[i],l[j]) for i in range(len(l)) for j in range(i+1,len(l)) if l[i]+l[j]==10])
def simple(a,b):
    """HI his is sample function"""
    return a+b
print(simple(5,10))
print(simple.__doc__)
di={"A":12,"B":12,"C":23}
# print(di.popitem())
l1=list(di.keys())
print(l1[-1],":",di[l1[-1]])
l=["p","y","t","h","o","n","5"]
# f=""
# for i in range(len(l)):
#     f=f+l[i]
# print(f)
print("".join(l))
t=["l","o","v","e"]
print("".join(t))
s='\"pu ram bala venkata Ramanjan\"'
print(s.split(" ",2))
print("/\\/\\/\\/\\/\\/\\")
print("/\\\\\\")