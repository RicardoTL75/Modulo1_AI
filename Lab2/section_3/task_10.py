print("\n\nOperations a = 5; b = 10")
# Arithmetic operations with integers
a = 5
b = 10

print("Integers:")
# ❌ Error 1: SyntaxError → missing parenthesis
print("a - b =", a - b, ", type:", type(a - b)   

# ❌ Error 2: TypeError → string + int
print("a + b =", "Result: " + (a + b), ", type:", type(a + b))

# ❌ Error 3: IndexError → wrong list index
numbers = [1, 2, 3]
print("Accessing index 5:", numbers[5])   # list has only 3 items

# ❌ Error 4: NameError → variable not defined
print("This variable does not exist:", total)
