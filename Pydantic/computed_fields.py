from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print('BMI: ', patient.calculated_bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted data')

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted data')

patient_data = {'name': 'Shuvom', 'email': 'abcd@null.com', 'age': 20, 'linkedin_url': 'https://www.linkedin.com/feed/', 'weight': 81.2, 'height': 1.72, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '1234509876', 'emergency': '1234509876'}}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)