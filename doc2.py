" More Control Flow Tools"

"1. if statement"

# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

"2.for Statements" 

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)  

# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)        


"3.The range() Function"

# for i in range(10):
#     print(i)

# print(list(range(5, 10)))


# print(list(range(0, 10, 3)))


# print(list(range(-10, -100, -30)))


# a = ['Mary', 'had', 'a', 'little', 'lamb','Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# print(sum(range(100)))   

"4.break and continue Statements & else Clauses on Loops"


# for n in range(2, 10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(" even number is", num)
#         continue
#     print(" odd number is ", num)

"5.pass "

# while True:
#     pass

# def initlog(*args):
#     pass 

# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case 401 | 403 | 404:
#              return "Not allowed"

# print(http_error(401 ))


# def describe_point(point):
#  match point:
#         case (0, 0):
#             return "Origin"
#         case (0, y):
#             return f"Y={y}"
#         case (x, 0):
#             return f"X={x}"
#         case (x, y):
#             return f"X={x}, Y={y}"

# print(describe_point((0,5)))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point") 

# print(where_is(Point(1,2)))

# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")


"6.Function "


# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# fib(2000)

# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b

#     return result

# f100 = fib2(100)    # call it
# print(f100)     


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)  

# print(ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!'))     

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
 
# print(f(3))


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# print(parrot('a million', 'bereft of life', 'jump'))    

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     print("-" * 40)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# print(cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch"))



# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)

# print(combined_example(1, standard=2, kwd_only=3))    

# def concat(*args, sep="  /  "):
#     return sep.join(args)

# print(concat("earth", "mars", "venus"))

  

# factorial
# n = int(input("enter number :"))
# f = 1
# while(n != 0):
#     f = f * n
#     n = n-1 
# print("factorial is :" ,f)

#Print a Fibonacci series 
# a, b = 0, 1
# while a < 54:
#     print(a, end=' ')
#     a, b = b, a+b
#     print()


# palindrom number 
# n = int(input("enter number :"))

# s=0
# m=n 

# while(n != 0):
#     r = n % 10
#     s = s*10 + r
#     n = n//10

# print("num is palindrom ")  if( m==s) else print(" num is not palindrom")

# armstong number
# n = int(input("enter number :"))

# s=0
# m=n 

# while(n != 0):
#     r = n % 10
#     s = s + (r*r*r)
#     n = n//10

# print("num is armstong ")  if( m==s) else print(" num is not armstong")


# n = int(input("enter number :"))

# s=0

# while(n != 0):
#     r = n % 10
#     s = s*10 + r
#     n = n//10

# print(s)
# while(s != 0):
#     r = s % 10
#     print(r)
#     s = s//10
    
 
# n = int(input("enter number :"))

# s=0

# while(n != 0):
#     r = n % 10
#     s = s*10 + r
#     n = n//10

# print(s)
# while(s != 0):
#     r = s % 10
#     if ( r== 0 ):
#         print("Zero",end =" ")
#     elif ( r== 1 ):
#         print("one",end =" ")   
#     elif ( r== 2 ):
#         print("two",end =" ")   
#     elif ( r== 3 ):
#         print("three",end =" ")
#     elif ( r== 4 ):
#         print("four",end =" ")
#     elif ( r== 5 ):
#         print("five",end =" ")
#     elif ( r== 6 ):
#         print("six",end =" ")

#     s = s//10

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)