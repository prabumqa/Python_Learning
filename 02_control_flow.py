# ============================================
# Python Basics: Control Flow
# ============================================

# --- If / Elif / Else ---
print("--- If/Elif/Else ---")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# --- Ternary Operator ---
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# --- For Loop ---
print("\n--- For Loop ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# Range
print("\nRange(5):")
for i in range(5):
    print(f"  i = {i}")

print("\nRange(2, 10, 2):")
for i in range(2, 10, 2):
    print(f"  i = {i}")

# Enumerate
print("\nEnumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# --- While Loop ---
print("\n--- While Loop ---")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1

# --- Break and Continue ---
print("\n--- Break ---")
for i in range(10):
    if i == 5:
        break
    print(f"  i = {i}")

print("\n--- Continue ---")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  Odd: {i}")

# --- Match Statement (Python 3.10+) ---
print("\n--- Match Statement ---")
command = "quit"
match command:
    case "start":
        print("  Starting...")
    case "stop":
        print("  Stopping...")
    case "quit":
        print("  Quitting...")
    case _:
        print("  Unknown command")

# --- Nested Loops ---
print("\n--- Multiplication Table (1-5) ---")
for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        row += f"{i*j:4}"
    print(row)
