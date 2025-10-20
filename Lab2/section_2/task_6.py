#*string.replace(old, new, count)
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

text = "70, 60, 78.9, 82"
result = text.replace("70, 60, 78.9, 82", "70, 9, 78.9, 82")
print("Calificacion final de Salvador Gomez", result)

text = "100, 50, 93.5, 78.8"
result = text.replace("100, 50, 93.5, 78.8", "100, 72.8, 93.5, 78.8")
print("Calificacion final de Sonia Infante", result) 

result= {}
for student, grades in result.items():
    average = sum(grades) / len(grades)
    result[student] = average
print(result)
