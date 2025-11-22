'''5.Design a module math_utils.py with functions:
factorial(n)
is_prime(n)
gcd(a,b)
Include exception handling for invalid or negative inputs. Import and test these functions from another script.
Concepts: Loops, recursion, functions, input validation.
'''
import math_utils
try:
    num1=int(input("ENTER A POSITIVE INTEGER FOR FACTORIAL:"))
    if num1<0:
        raise ValueError("NEGATIVE INPUT NOT ALLOWED")
    print(f"FACTORIAL OF {num1} IS: {math_utils.factorial(num1)}")
except ValueError as e:
    print(e)
try:
    num2=int(input("ENTER A POSITIVE INTEGER TO CHECK FOR PRIME:"))
    if num2<0:
        raise ValueError("NEGATIVE INPUT NOT ALLOWED")
    if math_utils.is_prime(num2):
        print(f"{num2} IS A PRIME NUMBER")
    else:
        print(f"{num2} IS NOT A PRIME NUMBER")
except ValueError as e:
    print(e)
try:
    num3=int(input("ENTER TWO POSITIVE INTEGERS FOR GCD:"))
    if num3<0:
        raise ValueError("NEGATIVE INPUT NOT ALLOWED")
except ValueError as e:
    print(e)
math_utils.factorial(5)
math_utils.is_prime(7)
math_utils.gcd(48, 18)
print("PROGRAM 5 COMPLETED")