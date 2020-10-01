'''
Python program to find factorial of given number
Factorial of n
n = n*(n-1)*(n-2)*(n-3).......3*2*1
4 = 4*3*2*1 = 24
'''


def factorial(n):
    # Line to Find Factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

# Driver Code


def factorial_init():
    num = int(input(" Enter Number For Factorial :\n"))
    answer = factorial(num)
    print(f"Factorial of {num} is {answer}.")

# Code For Solving Permutations


def permutation():
    print("Use This Logic To Input The Values 'xPy'\n")
    x = int(input("What is Your x value: "))
    y = int(input("What Is Your y Value: "))

    x_factorial = factorial(x)
    y_real = x - y
    y_factorial = factorial(y_real)

    permute = x_factorial / y_factorial
    print(f"{x} Permutation {y} is {permute}.")


task = int(input("Input: \n"
                 "1. For Finding Factorials.\n"
                 "2. For finding Permutations.\n"))
if task == 1:
    factorial_init()
else:
    permutation()
