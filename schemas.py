from pydantic import BaseModel, EmailStr


# DoctorCreate
# Représente les données requises pour l’inscription d’un médecin.

class DoctorCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

# DoctorLogin
# Utilisé lors de la connexion.

class DoctorLogin(BaseModel):
    username: str
    password: str

# PatientCreate
# Utilisé pour la création d’un nouveau patient et la prédiction du diabète.

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    glucose: float
    bmi: float
    bloodpressure: float
    pedigree: float
