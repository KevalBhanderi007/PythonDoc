# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))

# fruits.count('tangerine')

# fruits.index('banana')

# fruits.index('banana', 4)  # Find next banana starting at position 4

# fruits.reverse()
# fruits

# fruits.append('grape')
# fruits

# fruits.sort()
# print(fruits)

# fruits.pop()

squares = []
# for x in range(10):
#     squares.append(x**2)

# squares = list(map(lambda x: x**2, range(10)))


# squares = [round(x**2.89,x) for x in range(10)]

# print(squares)    

# del squares

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)
# print(f"{x.r} , {x.i}")


# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)

# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'
    
# N = int(input())
# arr=[]
# for i in range(N):
#     s=input()
#     if('insert' in s):
#         s=s.split()
#         arr.insert(int(s[1]),int(s[2]))
#     else:
#         print("invalid operation")
    
# D:\pyth doc\demo.txt

# f = open("demo.txt","r")
f = open("demo.txt","r+")
# demo = f.read(6)
# demo1 = f.readline()
# print(demo1)

# demo2 = f.readline()
# print(demo2)
# print(type(demo))
# f.close()  

# f =open("demo.txt","w")
# f = open("demo.txt","w+")

# f =open("demo.txt","a")
# f = open("demo.txt","a+")
# f.write("hii")
# f.close()

# with open("demo.txt","r") as l:
#     demo = l.read()

#     newdemo = demo.replace("bharat mata", "hindustan")
#     print(newdemo)
    
# with open("demo.txt","w") as l:
#     l.write(newdemo)
    # print(newdemo)

# import os 

# os.remove("d.ttt")    

# word = "ki"
# with open("demo.txt","r") as r:
#     data = r.read()
#     if(data.find(word) != -1):
#         print("word found")
#     else:
#         print("not exists")

# word = "hello"
# linenum = 1

# with open("demo.txt", "r") as f:
#     for line in f:
#         if word in line:
#             print(linenum)
#         linenum += 1    

# word = "hello"
# data = True
# linenum = 1

# with open("demo.txt","r") as f:
#     while data:
#         data = f.readline()
#         if(word in data):
#             print(linenum)
#         linenum += 1

# count = 0
# with open("demo.txt","r") as k :
#     data = k.read()

#     num = data.split(",")
#     for val in num :
#         if (int(val) % 2 == 0 ):
#             print(val)
#             count += 1

# print(count)
