# class Parent:
#     school="MHS"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self):
#         print(self.name,self.age)
#         print("Instance method of Parent")
#     @classmethod
#     def m2(cls):
#         print("Parent claassmethod")
#     @staticmethod
#     def m3():
#         print("Paent Satic method")
# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         super().m1()
#         super().m2()
#         super().m3()
#         print("#######################")
#     def show(self):
#         print(self.name)
#         super().m1()
#         super().m2()
#         super().m3()
# c=Child("bala",30)
# c.show()
# class Child1(Parent):
#     @classmethod
#     def sample(cls):
#         super().__init__(name,age)
#         super(Child1,cls).m1(cls)
#         super().m2()
#         super().m3()
#         print(super().school)
# ch=Child1("Rama",20)
# ch.sample()
# class Singleton:
#     _a=None
#     def __new__(cls):
#         if cls._a is None:
#             print("New instance ceate")
#             cls._a=super(Singleton,cls).__new__(cls)
#         else:
#             print("Already executed")
#         return cls._a
#     def __str__(self):
#         print("Overide")
# c=Singleton()
# c1=Singleton()
# print(c is c1)

# class Singleton:
#     _b=None
#     def __new__(cls):
#         if cls._b is None:
#             cls._b=super().__new__(cls)
#         return cls._b
# b1=Singleton()
# b2=Singleton()
# print(b1 is b2,"Single is state")
#dictionary
data={"a":[1,2,3],"b":[5,6,7]}
for i,k in data.items():
    print(i,k)
    c=1
    for l in k:
        c=c*l
    print(c)
for d,f in zip(data["a"],data["b"]):
        print(d*f)
                   





