from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'kolkata', 'state': 'West Bengal', 'pincode': '1234567'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Shuvom', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

# temp1 = patient1.model_dump()
temp1 = patient1.model_dump(include=['name', 'gender'], exclude={'address':['state']}, exclude_unset=True)
print(temp1)
print(type(temp1))

temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2))