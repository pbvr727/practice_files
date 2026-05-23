def decor(func):
    def inner(x,b):
        if x=="10" and b=="12":
            print(x+b)
        return func(x,b)
    return inner



@decor
def add(name,initial):
    print(name+" "+initial)
add("balaji","puvvada")
add("10","12")
def gen(o):
    for i in range(o):
        yield i
g=gen(10)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())