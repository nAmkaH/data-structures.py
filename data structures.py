Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Fibonacci(n):
...     if n < 0:
...         print("Invalid input")
...     elif n == 0:
...         return 0
...        elif n == 1 or n == 2:
...            return 1
...
...        else:
...             return Fibonacci(n-1) + Fibonacci(n-2)
...
...     print(Fibonacci(4))       
...             
...
