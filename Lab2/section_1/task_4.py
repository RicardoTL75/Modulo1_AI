grades_dictionary = {
    "Sonia Infante": [100, 50, 93.5, 78.8],
    "Cesar Inda": [100, 90.5, 100, 98.5],
    "Ricardo Torres": [72, 88, 91.5, 95],
    "Nayar Froylan": [95, 85, 87.2, 96],
    "Salvador Gomez": [70, 60, 78.9, 82],
    "America Guevara": [90.3, 75.6, 99, 80]
    }
# Create new dictionary with averages
average_grades = {}
for student, grades in grades_dictionary.items():
    average = sum(grades) / len(grades)
    average_grades[student] = average

print(average_grades)

# Print in column and alphabetical order
for student in sorted(average_grades.keys()):
    print(student, ":", average_grades[student])
