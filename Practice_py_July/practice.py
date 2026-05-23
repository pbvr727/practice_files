l=[10,2,3,4,1,0,-1]
for i in range(len(l)):
    for j in range(i+1,len(l)):
      if l[i]>l[j]:
         l[i],l[j]=l[j],l[i]
print(l)
s="puvvada bala venkata ramanjaneyulu"
for i in range(len(s)):
   print(s[i],end="\n")

# import datetime
# def decor(func):
#    def inner(a,b):
#         st=datetime.datetime.now()
#         c=a+b
#         print(c)
#         dt=datetime.datetime.now()
#         print(dt-st)
#         return func(a,b)
#     return inner
# @decor
# def add(a,b):
#    print(a,b)
# add(10,5)

d={"a":100,"b":20,"c":100}
for i,k in d.items():
   print(i,k)

s="thing";s1="night"

def simple(n):
    for u in range(n):
        for i in range(len(s2)):
            for j in range(i+1,len(s2)):
                if s2[i]>s2[j]:
                    s2[i],s2[j]=s2[j],s2[i]
    print(s2)
s2=list(s)
s1=list(s)
simple(2)
n=12345
r=0
while 0<n:
    d=n%10
    r=r*10+d
    n=n//10
print(r)


        