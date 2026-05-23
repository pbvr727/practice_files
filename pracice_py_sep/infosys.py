s=66
temp=s
r=0
while 0<s:
    d=s%10
    r=r*10+d
    s=s//10
if temp==r:
    print("palindrome")
else:
    print("not")

s="A4B6p4b5a2s3l2"
f=""
f1=""
t=""
for i in s:
    if i.isalpha():
        f=i
    else:
        f1=int(i)*f
        t=t+f1
print(t)

d={"a":100,"b":300}
for i in d.items():
    print(i)
d[300]=400
print(d)
s="puvvada bala venkata ramanjaneyulu"
# d={}
# for i in s:
#     if i not in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=d.get(i)
# print(d)
for i,l in enumerate(s):
    print(i,"=",l,end=",")
    if i==10:
        print(i,"ok")