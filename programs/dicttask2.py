

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}

}


for value in employees.values():
    print(value['name'] , value['department'])



for key,value in employees.items():
    print(value['name'],value['department'])