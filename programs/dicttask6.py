


students = [
    {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
    {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
]


for student in students:
    print(student['name'] , student['marks']['math'] , "," ,  student['marks']['science' ])

print("-----------")

for student in students:
    print(student['name'] ,list(student['marks'].values()))


alist = [10,20,30]
print(sum(alist))




students = [
    {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
    {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
]

for student in students:
    print(student['name'] , student['marks']['math'] ,  student['marks']['science'])