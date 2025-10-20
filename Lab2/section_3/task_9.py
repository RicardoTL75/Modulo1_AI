# Task 9-12: Example errors

# ❌ Error 1: SyntaxError (missing parenthesis)
print("Hello"   

# ❌ Error 2: TypeError (string + int not allowed)
s = "123"
num = 5
result = s + num   # string + int → TypeError

# ❌ Error 3: IndexError (invalid list index)
lst = [10, 20, 30]
print(lst[5])   # list has only 3 items (index 0, 1, 2)

# ❌ Error 4: NameError (variable not defined)
print(total)    # 'total' does not exist
