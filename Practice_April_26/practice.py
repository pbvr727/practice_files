# s=0
# while True:
#     print()
#     s=s+1
# print(s)
d={"a":100,"b":200,"c":300}
s="Puvvada Bala Venkata Ramanjaneyulu"
d1={}
for k,v in d.items():
    print("key",k,"value",v)
for i in range(len(s)):
    if s[i] in d1:
        d1[s[i]]=d1[s[i]]+1
    else:
        d1[s[i]]=1
print(d1)
s="3a5b6d"
u=""
for i in s:
    if i.isdigit():
        d=int(i)
    else:
        u=(i*d)+u
print(u)





