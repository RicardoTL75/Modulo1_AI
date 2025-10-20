print("----------------------\n")
#Ex. 1
s = [10, 20]
s *= 2
print(s) # Output: [10, 20, 10, 20]

#Ex. 2
print("----------------------\n")
s = ['a', 'b']
s *= 0
print(s) # Output: []

#Ex. 3
print("----------------------\n")
# Basic platform pattern for a level section
platform_pattern = ["ground", "empty", "coin", "empty"]
print("Basic pattern:", platform_pattern)

# Repeat the pattern to make a longer level section
platform_pattern *= 3
print("Extended section:", platform_pattern)
print("----------------------\n")