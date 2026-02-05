import csv
import json
import os

os.makedirs('data', exist_ok=True)

with open('data/students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'course', 'grade'])
    writer.writerow(['Alice', 'Python', '85'])
    writer.writerow(['Bob', 'Python', '92'])
    writer.writerow(['Charlie', 'Data1300', '78'])

print("Created data/students.csv")


data = [
    {'name': 'Alice', 'course': 'Python', 'grade': 85},
    {'name': 'Bob', 'course': 'Python', 'grade': 92},
    {'name': 'Charlie', 'course': 'Data1300', 'grade': 78}
    ]
with open('data/students.json', 'w') as f:
    json.dump(data, f, indent=4)
    print("Created data/students.json")
    print("Check the data/ folder to verify files!")    