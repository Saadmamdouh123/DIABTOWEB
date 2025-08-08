from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import conn, cursor, create_tables
from schemas import DoctorCreate, PatientCreate
from utils import hash_password, verify_password, predict_diabetes
from datetime import datetime

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
create_tables()

@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(username: str = Form(...), email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    if password != confirm_password:
        return "Passwords do not match"
    hashed = hash_password(password)
    cursor.execute("INSERT INTO doctors (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed))
    conn.commit()
    return RedirectResponse("/", status_code=302)

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    cursor.execute("SELECT id, password FROM doctors WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result and verify_password(password, result[1]):
        response = RedirectResponse("/home", status_code=302)
        response.set_cookie("doctor_id", str(result[0]))
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Identifiants incorrects"})

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/add", response_class=HTMLResponse)
def add_patient_form(request: Request):
    return templates.TemplateResponse("add_patient.html", {"request": request})

@app.post("/submet")
def submit_patient(request: Request,
                   name: str = Form(...),
                   age: int = Form(...),
                   sex: str = Form(...),
                   glucose: float = Form(...),
                   bmi: float = Form(...),
                   bloodpressure: float = Form(...),
                   pedigree: float = Form(...)):
    doctor_id = int(request.cookies.get("doctor_id"))
    features = [glucose, bmi, age, pedigree] 
    result = int(predict_diabetes(features))
    cursor.execute("""
    INSERT INTO patients (doctorid, name, age, sex, glucose, bmi, bloodpressure, pedigree, result)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    """, (doctor_id, name, age, sex, glucose, bmi, bloodpressure, pedigree, result))
    patient_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO predictions (patientid, result) VALUES (%s, %s)", (patient_id, result))
    conn.commit()
    return RedirectResponse("/patients", status_code=302)

@app.get("/patients", response_class=HTMLResponse)
def view_patients(request: Request):
    doctor_id = int(request.cookies.get("doctor_id"))
    cursor.execute("SELECT * FROM patients WHERE doctorid = %s", (doctor_id,))
    patients = cursor.fetchall()
    total = len(patients)
    diabetic = sum(1 for p in patients if p[9] == 1)
    percent = (diabetic / total * 100) if total > 0 else 0
    return templates.TemplateResponse("patients.html", {"request": request, "patients": patients, "percent": percent})

@app.get("/delete/{id}")
def delete_patient(id: int):
    cursor.execute("DELETE FROM patients WHERE id = %s", (id,))
    conn.commit()
    return RedirectResponse("/patients", status_code=302)

