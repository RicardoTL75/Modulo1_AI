print("\nFinding maximun, minimum value & length for team #5!")

list = [3, 1, 4, 1, 5, 9, 2, 6, 13, 8, 21, 0.5, 50, 0.001]

def analyze_task3(seq):
    # Find maximum value
    max_val = seq[0]
    for element in seq:
        if element > max_val:
            max_val = element
    
    # Find minimum value
    min_val = seq[0]
    for element in seq:
        if element < min_val:
            min_val = element
    
    # Find length
    length = 0
    for _ in seq:
        length += 1
    
    return max_val, min_val, length

max_value, min_value, length = analyze_task3(list)

print(f"\nList: {list}")
print(f"\nMaximum value: {max_value}")
print(f"\nMinimum value: {min_value}")
print(f"\nLength: {length}")