from pydantic import BaseModel, EmailStr

class DoctorCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

class DoctorLogin(BaseModel):
    username: str
    password: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    glucose: float
    bmi: float
    bloodpressure: float
    pedigree: float
