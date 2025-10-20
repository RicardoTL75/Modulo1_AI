print("\nFinding maximun, minimum value & length for team #5!")

list = [3, 1, 4, 1, 5, 9, 2, 6, 13, 8, 21, 0.5, 50, 0.001]

def analyze_task3(seq):
    # ❌ Error 1: NameError → wrong variable name "sq" instead of "seq"
    max_val = sq[0]  
    
    for element in seq:
        if element > max_val:
            max_val = element
    
    # ❌ Error 2: TypeError → comparing number with string
    min_val = seq[0]
    for element in seq:
        if element < "wrong":   # string vs number
            min_val = element
    
    # ❌ Error 3: IndexError → forcing out of range index
    print("Accessing element 99:", seq[99])
    
    # ❌ Error 4: Logical mistake → length calculation wrong
    length = 0
    for _ in seq:
        length -= 1   # should be +1
    
    return max_val, min_val, length


# This line will not run correctly because of the errors above
max_value, min_value, length = analyze_task3(list)

print(f"\nList: {list}")
print(f"\nMaximum value: {max_value}")
print(f"\nMinimum value: {min_value}")
print(f"\nLength: {length}")
