from passlib.hash import bcrypt
import pickle

# Fonctions de sécurité (mot de passe)
# hash_password(password: str) -> str
# Hache un mot de passe en utilisant l'algorithme bcrypt.

def hash_password(password):
    return bcrypt.hash(password)

# verify_password(password: str, hashed: str) -> bool
# Vérifie qu’un mot de passe correspond bien à un hachage donné

def verify_password(password, hashed):
    return bcrypt.verify(password, hashed)

#Chargement du modèle .pkl

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# predict_diabetes(data: list[float]) -> int
# Fait une prédiction à partir d’une liste de caractéristiques cliniques.

def predict_diabetes(data):
    prediction = model.predict([data])
    return int(prediction[0])
