# import math


# def circle_area(radius):
#     if radius < 0:
#         return 0
#     else:
#         area = math.pi * radius**2
#         print(f"Area is {area}")
#         return area


# circle_area(5)

# main.py
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci number:", fibonacci(10))
