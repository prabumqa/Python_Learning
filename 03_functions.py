# ============================================
# Python Basics: Functions
# ============================================

# --- Basic Function ---
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

print(greet("Alice"))

# --- Default Parameters ---
def power(base, exponent=2):
    return base ** exponent

print(f"3^2 = {power(3)}")
print(f"3^4 = {power(3, 4)}")

# --- *args (Variable Positional Arguments) ---
def add_all(*args):
    return sum(args)

print(f"Sum of 1,2,3,4,5 = {add_all(1, 2, 3, 4, 5)}")

# --- **kwargs (Variable Keyword Arguments) ---
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nUser Info:")
print_info(name="Bob", age=30, city="NYC")

# --- Lambda Functions ---
print("\n--- Lambda Functions ---")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Sort with lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students_sorted = sorted(students, key=lambda s: s[1], reverse=True)
print(f"Sorted by score: {students_sorted}")

# --- Map, Filter, Reduce ---
print("\n--- Map, Filter, Reduce ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# Reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# --- Closures ---
print("\n--- Closures ---")
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# --- Decorators ---
print("\n--- Decorators ---")
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    total = sum(range(1000000))
    return total

result = slow_function()
print(f"  Result: {result}")

# --- Generator Functions ---
print("\n--- Generators ---")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_sequence = list(fibonacci(10))
print(f"Fibonacci(10): {fib_sequence}")

# --- Recursive Function ---
print("\n--- Recursion ---")
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
