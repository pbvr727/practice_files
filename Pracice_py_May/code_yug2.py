# with open("hi.txt","w") as f1:
#     f1.write("Hello \n")
#     f1.write("Hello I AM GOOD \n")
#     f1.write("i am single \n")
# with open("hi.txt") as f2:
#     r=f2.read()
#     w=0
#     for i in r.split():
#         print(i)
#         w=w+1
#     print(w)
#########prime numbers#############
# l=[]
# for i in range(2,26):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(l)
# for i in l:
#     print(i)
# if (2 and 7) in i:
#     print(i,"ok")
##############################################
# l=[0,3,1,4,3,7,6,9,2]
# l2=[]
# l3=[]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         l2.append((l[i]*l[j]))
#         l3.append((i,j))
# print(l2)
# o=l2[0]
# for i in range(len(l2)):
#     if l2[i]>o:
#         o=l2[i]
# print(o)
##########################################
# max pair
l=[0,3,1,4,3,7,6,9,2]
l1=l[0]
l2=l[1]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i]*l[j])>(l1*l2):
            print(l1*l2,l1,l2,"CODE DESRIPTION")
            l1=l[i]
            l2=l[j]
print(l1,l2)
#################################
# l=[2,7,11,5]
# l=[3,3]
# target=6
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print([i,j])
# s="Ramanjaneyulu"
# for i in range(len(s)-1):
#     d=abs(ord(s[i])+ord(s[i+1]))
# print(d)
#########decor##################333
def decor(func):
    def inner(*args,**kwargs):
        print("Hi")
        r=func(*args,**kwargs)
        return r
    return inner
@decor
def simple(a,b,d,c):
    print(c)
    return a+b+d
print(simple(3,5,3,8))
####################################
# import time
# def decor(func):
#     def inner(x,y):
#         s=time.time()
#         if x=="reshma":
#             print("Yarla sai")
#         else:
#             return func(x,y)
#         e=time.time()
#         print(e-s)
#     return inner
# @decor
# def add(name,age):
#     print(name+age)
# print(add("balaji","puvvada"))
# print(add("reshma","sai"))

# def decor(func):
#     def inner(*args,**kwargs):
#         print(*args,**kwargs)
#         return func(*args,**kwargs)
#     return inner
# @decor
# def add(name,b,age):
#     return name,age
# print(add("balu",100,age=20))