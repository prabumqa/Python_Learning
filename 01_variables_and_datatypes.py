# ============================================
# Python Basics: Variables and Data Types
# ============================================

# --- Variables ---
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# --- Data Types ---
print("\n--- Data Types ---")
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# --- Type Conversion ---
print("\n--- Type Conversion ---")
x = "100"
y = int(x)          # str to int
z = float(x)        # str to float
print(f"String: {x}, Int: {y}, Float: {z}")

# --- Multiple Assignment ---
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# --- Constants (convention: UPPERCASE) ---
PI = 3.14159
MAX_SIZE = 100

# --- None Type ---
result = None
print(f"Result is: {result}, Type: {type(result)}")

# --- String Operations ---
print("\n--- String Operations ---")
text = "Hello, Python!"
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Slice [0:5]: {text[0:5]}")
print(f"Replace: {text.replace('Python', 'World')}")
print(f"Split: {text.split(', ')}")

# --- Number Operations ---
print("\n--- Number Operations ---")
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")       # float division
print(f"10 // 3 = {10 // 3}")     # floor division
print(f"10 % 3 = {10 % 3}")       # modulus
print(f"10 ** 3 = {10 ** 3}")     # exponent
