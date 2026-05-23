# l=[2,3,4,3,4,9,1] 
# d={}
# for i,k in enumerate(l):
#     print(i,k)
#     if l.count(k)>1:
#         if k==
#         d[k]=i
# print(d)
d=["bat","act","cat","god","night","tab","thing","dog"]# output is [["bat","tab"],["act","cat"]]
# l=[]
# for i in d:
#     y=sorted(i)
#     f="".join(y)
# y1=f[0]
# for j in d:
#     if j==y1:
#         print("anagram")
#         l.append([j,y1])
# print(l)
# s="puvvada bala venkaa ramanjaneyulu"
# for i in s:
#     print(i)
d1=d[0]
l1=[]
for i in range(len(d)):
#     if sorted(d[i])==sorted(d1[]):
#         l1.append([d[i],d1])
       
#     else:
#         d1=d[i]
      
# l1.append([d[i],d1])
# print(l1)
    for j in range(i+1,len(d)):
        if sorted(d[i])==sorted(d[j]):
            l1.append([d[i],d[j]])
print(l1)



import datetime
def decor(func):
    def inner(x,y):
        begin=datetime.datetime.now()
        print("hello")
        
        end=datetime.datetime.now()
        total=end-begin
        print(total)
        return func(x,y)
    return inner

@decor
def add(x,y):
    c=x+y
add(5,10)
students = [{'name': 'John', 'scores': {'Math': 90, 'Science': 85, 'English': 95}},
        {'name': 'Alice', 'scores': {'Math': 80, 'Science': 95, 'English': 92}},
        {'name': 'Bob', 'scores': {'Math': 92, 'Science': 87, 'English': 89}},
        {'name': 'Carol', 'scores': {'Math': 88, 'Science': 94, 'English': 90}}
        ]
t=0
l=[]
for i in range(len(students)):
    
    s=sum(students[i]['scores'].values())
    le=
    mar=s//le
print(mar)

print(max(mar))


