# def insert_patient_data(name, age):
#     print(name)
#     print(age)
#     print('Inserted into database')

# insert_patient_data('Shuvom', 'twenty') # the input type of age should be numeric but here it is string (type error)


# def insert_patient_data(name: str, age: int):
#     print(name)
#     print(age)
#     print('Inserted into database')

# insert_patient_data('Shuvom', 20)

# def insert_patient_data(name, age):
#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError('Age cannot be negative')
#         else:
#             print(name)
#             print(age)
#             print('Inserted into database')
#     else:
#         raise TypeError("Incorrect data type")

# insert_patient_data('Shuvom', 20)

# def update_patient_data(name, age):
#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError('Age cannot be negative')
#         else:
#             print(name)
#             print(age)
#             print('Inserted into database')
#     else:
#         raise TypeError("Incorrect data type")

# update_patient_data('Shuvom', 20)




from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated into database')

patient_info = {'name': 'Shuvom', 'age': 20}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)
print(f"The age of {patient1.name} is {patient1.age}")

update_patient_data(patient1)
print(f"The age of {patient1.name} is {patient1.age}")