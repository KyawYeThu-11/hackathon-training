# Reads a CSV file into a list of dict objects
# # We want to get a list of dictionaries (a list of students' info)
students = []


# with open('students.csv') as file:
#     for line in file:
#         print(line)

# with open('students.csv') as file:
#     for line in file:
#         name, age, gender, course = line.split(',')
#         print(name, age, gender, course)
        
with open('students.csv') as file:
    next(file)
    for line in file:
        name, age, gender, course = line.rstrip().split(',')
        students.append({'name': name, 'age': age, 'gender':gender, 'course':course})

print(students)

# # Using csv module
# import csv

# students = []

# with open('students.csv') as file:
#     reader = csv.DictReader(file)
#     for line in reader:
#         students.append({'name': line['Name'], 'age': line['Age'], 'gender':line['Gender'], 'course':line['Course']})

# print(students)

