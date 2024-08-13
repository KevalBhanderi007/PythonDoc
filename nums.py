# def is_armstrong(number):
#     digits = [int(d) for d in str(number)]
#     power = len(digits)
#     return number == sum(d ** power for d in digits)

# # Example usage
# for num in range(10):
#     if is_armstrong(num):
#         print(f"{num} is an Armstrong number")


# def is_prime(number):
#     if number <= 1:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# # Example usage
# for num in range(1, 10):
#     if is_prime(num):
#         print(f"{num} is a prime number")


# def is_perfect(number):
#     if number < 2:
#         return False
#     divisors = [1]
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             divisors.append(i)
#             if i != number // i:
#                 divisors.append(number // i)
#     return sum(divisors) == number

# # Example usage
# for num in range(1, 10):
#     if is_perfect(num):
#         print(f"{num} is a perfect number")


# def fibonacci(n):
#     a, b = 0, 1
#     result = []
#     while a <= n:
#         result.append(a)
#         a, b = b, a + b
#     return result

# # Example usage
# print(fibonacci(10))  # Generate Fibonacci numbers up to 100


# import math

# def factorial(n):
#     return math.factorial(n)

# # Example usage
# for i in range(10):
#     print(f"Factorial of {i} is {factorial(i)}")


# def is_palindrome(number):
#     s = str(number)
#     return s == s[::-1]

# # Example usage
# for num in range(10):
#     if is_palindrome(num):
#         print(f"{num} is a palindrome number")


# def is_square(number):
#     root = int(number ** 0.5)
#     return root * root == number

# # Example usage
# for num in range(1, 10):
#     if is_square(num):
#         print(f"{num} is a square number")


# def is_triangular(number):
#     if number < 1:
#         return False
#     # Using the formula: n(n+1)/2 = number
#     # Solve the quadratic equation: n^2 + n - 2*number = 0
#     import math
#     discriminant = 1 + 8 * number
#     sqrt_disc = math.isqrt(discriminant)
#     return sqrt_disc * sqrt_disc == discriminant and (sqrt_disc - 1) % 2 == 0

# # Example usage
# for num in range(1, 10):
#     if is_triangular(num):
#         print(f"{num} is a triangular number")



# def  getdisc (age : int) -> bool:
#     if  age < 18 or age >= 65:
#         return True
#     else:
#         return False
    # return False

# print(getdisc(12))


# for i in reversed(range(0,11)):
#     print(i)


# for i in range(0,11):
#     break
#     print(i)

# word = "sjhgjgjhf jyhvrf"
# print(word[len(word)-1])

# for i in range(len(word)):
#     print(i,word[i])

# for char in word:
#     print(char)

# word = "dfjch jrsb ube kbnrjf uibud"
# count ={}
# for char in word:
#     if char not in count:
#         count[char] = 1
#     else :
#         count[char] += 1 
# print(count)   

# from datetime import datetime
# now = datetime.now()
# print(now)

# from datetime import datetime , timedelta
# dt = datetime(2024, 8, 5)
# delta = timedelta(days=5)
# print(dt)
# print(delta)

# import random
# rand_num = random.randint(1, 10)
# print(rand_num)

# import webbrowser
# webbrowser.open('http://google.com')


# weight = int(input("weight :"))
# unit = input("(L)bs or (K) g:")
# if unit.upper() == "L":
#     convert  = round(weight * 0.45,3)
#     print(f"your weight {convert} kilos")
# else :
#     convert  =  weight // 0.45
#     print(f"your weight is {convert} pounds") 

# import random
# rand_num = random.randint(1, 10)
# # rand_num = 8
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess Number : "))
#     guess_count += 1 
#     if guess == rand_num:
#         print("You Won!")
#         break
# else:
#     print("Sorry try again")        

# command = ""
# started = False

# while True:
#     command = input("-> ").lower()
#     if command == "start":
#         if started :
#             print(" car is already start!!")
#         else:
#             started = True
#             print("car is start.....")
#     elif command == "stop":
#         if started :
#             print(" car is already stop!!")
#         else:
#             started = True
#             print("car is stop.....")
#     elif command == "help":
#         print("""
# start -  to start 
# stop  -  to stop
# quit  -  to quit 
# """) 
#     elif command == "quit":
#         break 
#     else :
#         print("sorry try again")

# print("hello good morning!!  😊")
 
# import pandas as pd
# musicdata = pd.read_csv("music.csv")

# print(musicdata)