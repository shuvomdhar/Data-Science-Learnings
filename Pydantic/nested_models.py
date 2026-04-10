from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'kolkata', 'state': 'West Bengal', 'pincode': '1234567'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Shuvom', 'gender': 'male', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.pincode)