from passlib.hash import bcrypt
import pickle

def hash_password(password):
    return bcrypt.hash(password)

def verify_password(password, hashed):
    return bcrypt.verify(password, hashed)

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_diabetes(data):
    prediction = model.predict([data])
    return int(prediction[0])
