# def decor(func):
#     def wrapper(user_name):
#         if 'admin' in user_name:
#             return "access Denied"
#         return func(user_name)
#     return wrapper


# @decor
# def login(user_name):
#     return f"{user_name} successfully login"
# print(login("balaji"))
# print(login("myadmin"))
#############################################
#AGE Validation function
def decor(func):
    def wrapper(Age):
        if Age >18:
            return "You are eligble to creaeded egistration "
        else:
            return func(Age)
    return wrapper


@decor
def verify(Age):
    if Age<18:
        return "the user is not eligble"
print(verify(15))
print(verify(20))
