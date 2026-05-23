l=[1,2,3]
l1=[5,6,7]
print(l+l1)
l.append(l1)
print(l)
l.extend(l1)
print(l)

# def add(x,y):
#     for i in range(x,y):
#         print(i)
# add(3,5)
def fact(n):
    t=0
    for i in range(1,n):
        print("total3",t,i)
        t=t+i
        print("total",t,i)
        print(t)
fact(5)
import functools
l=[10,12,11,6,1,2,3,4,5,5,6,7,8,9,10]
print([i for i in l if i%2==0])
print(list(map(lambda x:x*2,l)))
print(list(filter(lambda x:x%2==0,l)))
print(functools.reduce(lambda x,y:x*y,l))
l2=[]
for i in range(len(l)):
    # print(l[i],end="@")
    for j in range(i+1,len(l)):
        if l[i]+l[j]==15:
           l2.append(l[i]+l[j])
           print(l[i],l[j])
# print(l)
print(l2)
d="8008887078"
d1=""
for i in range(len(d)-1,-1,-1):
    d1=d[i]+d1
    print(d1)
d=8008887078
r=0
while d<0:
    digi=d%10
    r=r+digi
    d=d//10
print(r)
l=[]
for i in range(2,100):
    for j in range(2,int(i*0.5)+1):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


def rec(p):
    l=[]

    for i in p:
        if isinstance(i,list):
            l.extend(rec(i))
        else:
            l.append(i)

    return l
p=[[2,3],5,6,[7,8,9],11]
print(rec(p))

g=[2,3,5,6,7,8,9,10,12]
for i in range(len(g)):
    for j in range(i+1,len(g)):
        if g[i]+g[j]==15:
            print(g[i],g[j])

s="ramanjaneyulu"
s1=""
for i in s:
    s1=i+s1
print(s1)

