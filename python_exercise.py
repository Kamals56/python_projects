"""
# star triangle
def print_triangle(height: int, p_char: str = '*', e_char: str = ' '):
  for i in range(1, height * 2, 2):
    spaces = (height - (i // 2) - 1) * e_char
    stars = i * p_char
    print(spaces + stars)
    
  
print_triangle(6)
print_triangle(10)

# index of the highest value in matrix
def find_high(matrix: list[list[int]]) -> tuple[int, int]:
    max_value = matrix[0][0]
    max_index = (0, 0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)
    
    return max_index

matrix = [
  [1, 5, 7],
  [9, 3, 1],
  [0, 1, 1]
]

print(find_high(matrix))


#3 Palindrome or not
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

print(is_palindrome("mom"))
print(is_palindrome("MADAM"))



#Fibbonacci sequence
num = int(input("Enter the number: "))
a, b = 0, 1
if num == 1:
    print(a)
elif num == 2:
    print(a, b)
else:
    print(f"{a} {b}", end=" ")

    for i in range(num - 2):
        c = a + b
        print(c, end=" ")

        a, b = b, c


#4 Finding nth term of fibonacci sequence
def nth_fibonacci(n: int) -> int:
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

print(nth_fibonacci(10))  



#5 Random integer
import random

def random_numbers_to_dict() -> dict:
    positive = []
    negative = []
    zero = []

    for _ in range(100):
        num = random.randint(-50, 50)
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        else:
            zero.append(num)
    return {
        "positive": positive,
        "negative": negative, 
        "zero": zero
    }

result = random_numbers_to_dict()
print(f"positive: {result['positive']}\n")
print(f"negative: {result['negative']}\n")
print(f"zero: {result['zero']}\n")

"""
import time
from typing import Callable, Any, Dict

def cache_results(func: Callable[[int], int]) -> Callable[[int], int]:
    cache: Dict[int, int] = {}
    def wrapper (n: int) -> int:
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper


@cache_results
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial (n -1)

factorial(100)

def time_function(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return (result, elapsed_time)

def test_factorial_coaching(n: int= 35):
    result, elapsed_time = time_function(factorial, n)
    print(f"first call: factorial((n)), took {elapsed_time:.6f} seconds")
    
    result, elapsed_time = time_function(factorial, n)
    print(f"second call: factorial({n}), took {elapsed_time:.6f} seconds")
    
test_factorial_coaching()