# def funone(a,b):
#     print(a,b)
#
# f = funone(input(),input())
# print(f)

# def funOne(a=input(),b=input()):
#     print(a,b)
#
# print(funOne())
from sys import argv
def deco(func):
    def deco1(*args):
        l = []
        args = input()
        args = list(args.split( ))
        for i in args:
            if "." in i:
                i = float(i)
                l.append(i)
            elif i.isalpha():
                l.append(i)
            elif i.isnumeric():
                i = int(i)
                l.append(i)
        return func(l)
    return deco1()

@deco
def funOne(a):
    return a
print(funOne)

# try:
#     val = funOne()
#     print(val)
# except TypeError as err:
#     print(err)

# def deco(func):
#     def deco1(a=input(),b=input()):
#         return func(a,b)
#     return deco1()
#
# @deco
# def funOne(a,b):
#     #print(a,b)
#     return (a,b)
#
# val =funOne()
# print(val)
