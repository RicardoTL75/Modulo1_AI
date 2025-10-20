print("----------------------\n")
#Example 1: Basic Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

print("----------------------\n")
#Example 2: Input Without Prompt
color = input()
print(f"You entered: {color}")

print("----------------------\n")
#Example 3: CRITICAL POINT: input() always returns a string, even if the user types numbers!
age = input("Enter your age: ")
print(f"Type of age: {type(age)}")
print(f"Value: {age}")

print("----------------------\n")
#Example 4: Converting to Numbers
# Convert to integer
age = int(input("Enter your age: "))
print(f"In 10 years, you'll be {age + 10} years old")

# Convert to float
price = float(input("Enter product price: "))
print(f"With tax: ${price * 1.10:.2f}")