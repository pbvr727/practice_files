s="puvvada bala venkata ramanjaneyulu"
s[-10]#a
for k,v in enumerate(s,start=0):
    print(k,"=",v," ",end="\n")
print(s[-20:-30:-1])
print(s[::-1])
p=""
for i in s:
    p=i+p
print(p)
l=[1,2,3,4,5]
l1=[1,2,3,4,5]
print([x+y for x,y in zip(l,l1)])
l=[10,11,9,7,8,3,4,1,0]
for i in range(len(l)):
    for j in range(i,len(l)-1):
        if l[i]>l[j+1]:
            l[i],l[j+1]=l[j+1],l[i]
print(l[-1])
print(l[-3])
import sys
l=["sita",2,3,4,5]
l1="Rama",2,3,4,5
print(sys.getsizeof(l));print(sys.getsizeof(l1))
import datetime
def decor(func):
    def inner(a,b):
        if a+b==20:
            dt=datetime.datetime.now()
            print(dt)
        else:
            return func(a,b)
    return inner

@decor
def simple(a,b):
    return a+b,a-b
print(simple(10,5))
print(simple(15,5))
x=10
def pos(y,z):
    """i can creae global valriable and perform changes"""
    print(y+z)
    # print("gloabla=",x)
    global x
    x=25
    print("change",x)
pos(10,20)
print(pos.__doc__)
s=lambda a:"even" if a%2==0 else "odd" 
print(s(3))
  

    