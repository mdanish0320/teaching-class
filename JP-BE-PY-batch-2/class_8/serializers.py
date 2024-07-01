import json

employees = [
    {
     "name": "danish"   
    },
    {
        "name": "Amin"
    },
    {
        "name": "Talha"
    }
]

print(employees, type(employees))
print(employees[0]['name'])
employee_str = json.dumps(employees)
print(employee_str, type(employee_str))
# print(employee_str[0]['name'])

f = open("employee.json", "wt")
f.write(employee_str)
f.close()

f = open('employee.json', "rt")
data = f.read()
f.close()

print(data)
data = json.loads(data)
print(data[0]['name'])

################################
################################
################################
import pickle

employees = [
    {
     "name": "danish"   
    },
    {
        "name": "Amin"
    },
    {
        "name": "Talha"
    }
]


print(employees, type(employees))
print(employees[0]['name'])
employee_byte = pickle.dumps(employees)
print(employee_byte, type(employee_byte))
# print(employee_str[0]['name'])

f = open("employee.bin", "wb")
f.write(employee_byte)
f.close()


f = open('employee.bin', "rb")
data = f.read()
print(data)
f.close()

data = pickle.loads(data)
print(data[0]['name'])