def add(x,y):
    z=x+y
    print("Bagunaru")
    return z
print("Hello")
print(add(10,5))
#Sum of numbers
def sum_of_num(n):
    y=1
    for i in range(1,n):
        y=y*i
    print(y)
print(sum_of_num(15))
#6️⃣ Word frequency
# word_count("hello hello world")
# → {'hello': 2, 'world': 1}
def count1(s):
    for i in s.split():
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
    return d
s="puvvada bala vebkata ramajnaneuioko balu bala venkata"
d={}
print(count1(s))
#Count vowels in a string
def vowels1(s,s2):
    l=[]

    for i in s:
         if i not in s2:
              l.append(i)
    return l,len(l)
s="Anil Ravipudi Mana Shankar Vara Praqsad garu"
s2="eioua"
print(vowels1(s,s2))
#decoator function
@decor
def add(s,b):
    print(s+b)
add(3,5)
              
     
     
