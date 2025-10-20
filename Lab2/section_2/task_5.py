grades_dictionary = {
    "Sonia Infante": [100, 50, 93.5, 78.8],
    "Cesar E. Inda": [100, 90.5, 100, 98.5],
    "Ricardo Torres": [72, 88, 91.5, 95],
    "Nayan Froylan": [95, 85, 87.2, 96],
    "Salvador Gomez": [70, 60, 78.9, 82],
    "America Guevara": [90.3, 75.6, 99, 80]
}

# Create new dictionary with averages
average_grades = {}
for student, grades in grades_dictionary.items():
    average = sum(grades) / len(grades)
    average_grades[student] = average

# Sort by grade in descending order (highest first)
average_grades_high = dict(sorted(average_grades.items(), key=lambda item: item[1], reverse=True))
   
# Sort by grade in descending order (lowest first)
average_grades_low = dict(sorted(average_grades.items(), key=lambda item: item[1]))

# Sort alphabetical order
average_grades_alph = dict(sorted(average_grades.items(), key=lambda item: item[0]))

# Print names and grades in cascade (one per line)
print("\nHigh to Low")
for student, average in average_grades_high.items():
    print(student, ":", average)


print("\nLow to High")    
for student, average in average_grades_low.items():
    print(student, ":", average)
    

print("\nNames in Alphabetical Order")      
for student, average in average_grades_alph.items():
    print(student, ":", average)