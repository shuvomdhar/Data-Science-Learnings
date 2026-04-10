from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters', examples=['Harish', 'Rajiv'])]
    email: EmailStr
    age: int = Field(gt=0, lt=120)
    linkedin_url: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not?')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.linkedin_url)
    print(patient.married)
    print(patient.allergies)
    print('Inserted data')

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted data')

patient_data = {'name': 'Shuvom', 'email': 'abcd@null.com', 'age': 20, 'linkedin_url': 'https://www.linkedin.com/feed/', 'weight': 81.2, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '1234509876'}}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)