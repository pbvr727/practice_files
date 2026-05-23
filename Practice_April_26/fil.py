# print("hello")
# d=["jk","jk","kl","opi"]
# for i in d:
#     print(i)
# x=[1,2,3]
# for i in x:
#     x.remove(x[i])
# print(x)#[2,3][]

import datetime
def decor1(func):
    def inner(*x,**y):
        s=datetime.datetime.now()
        t=0
        for i in x:
            t=t+i
            print(t)
        end=datetime.datetime.now()
        return end-s,func(*x,**y)
    return inner
        
@decor1
def add(s,n):
    print("Hello",s,n)
print(add(3,8.10,13))