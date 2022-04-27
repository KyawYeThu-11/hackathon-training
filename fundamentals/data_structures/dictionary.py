# # A Single Dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# indexing
print(students['Draco'])

# # Simple iteration
# for student in students:
#     print(student)

# # Iterating while getting values and keys
# for student, house in students.items():
#     print(f'{student} is from the house, {house}.')

# for student in students:
#     print(f'{student} is from the house, {students[student]}.')

# # adding
# students['Harry'] = 'Slytherin'
# students['Snape'] = 'Slytherin'
# print(students)

# Combination of list and dictionary
students = [
    {"name": "Hermione", "major": "Physics", "age": 21},
    {"name": "Harry", "major": "Physics", "age": 19},
    {"name": "Ron", "major": "Physics", "age": 17},
    {"name": "David", "major": "Business", "age": 18},
]


# Demonstrates iterating over a list of dict objects
for student in students:
    print(student["name"], student["major"], student["age"], sep=", ")



