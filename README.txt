📝 Rapport de Projet — DiabetoWeb

# 1. 📌 Contexte Général

DiabetoWeb est une startup marocaine spécialisée dans l’innovation numérique en santé. Ce projet a pour ambition de faciliter la gestion des dossiers médicaux des patients et d’améliorer le dépistage du diabète à l’aide de l’intelligence artificielle (IA).

L’objectif est de développer une application web complète, intuitive et sécurisée permettant à un médecin de :

Gérer efficacement les dossiers de ses patients,

Analyser les données cliniques importantes,

Utiliser un modèle prédictif basé sur le machine learning pour évaluer le risque de diabète,

Accéder à un tableau de bord centralisé.

# 2. 🎯 Objectifs du Projet

Digitaliser la gestion des patients dans un cadre médical sécurisé.

Intégrer un modèle d’IA dans une solution web pour assister le diagnostic.

Faciliter le suivi médical à travers une interface intuitive.

Offrir une base solide pour une future plateforme de santé intelligente.

# 3. 👨‍⚕️ Fonctionnalités Réalisées

🔐 Authentification des Médecins
Création de compte et connexion sécurisée.

Vérification des identifiants via base PostgreSQL.

Redirection et gestion des erreurs.

# 👥 Gestion des Patients

Ajout, affichage et suppression de patients.

Enregistrement de données cliniques : âge, sexe, glucose, IMC, pression artérielle, etc.

Lien entre chaque patient et le médecin créateur.

# 🤖 Prédiction du Diabète

Intégration d’un modèle .pkl pré-entraîné (Machine Learning).

Chargement du modèle au lancement de l’application.

Prédiction automatique du risque (0 : non-diabétique, 1 : diabétique).

Enregistrement des résultats en base de données.

# 📊 Tableau de Bord

Visualisation synthétique des patients.

Filtres par statut diabétique ou date.

Statistiques simples : taux de patients à risque.

Bouton rapide pour ajouter un patient.

# 4. ⚙️ Stack Technologique

| Composant              | Technologie Utilisée      |
| ---------------------- | ------------------------- |
| Backend                | FastAPI (Python)          |
| Frontend               | HTML, CSS, Jinja2         |
| Base de Données        | PostgreSQL                |
| Machine Learning       | Modèle entraîné (XGBoost) |
| Validation des données | Pydantic (FastAPI)        |
| Session (optionnelle)  | fastapi\_login ou Cookies |

# 5. 🗃️ Structure de la Base de Données
Table medecins
id, username, email, password, created_at

Table patients
id, doctorid, name, age, sex, glucose, bmi, bloodpressure, pedigree, result, created_at

Table predictions
id, patientid, result, created_at

# 6. ✅ Validation des Données
Grâce à Pydantic, les données saisies sont validées avant traitement :

Vérification des types (int, float, str),

Valeurs acceptées uniquement (ex. sexe = "male"/"female"),

Données cliniques obligatoires et normalisées.

9. 📂 Organisation du Code

DiabetoWeb/
│
├── main.py                 # Code FastAPI principal
├── model.pkl               # Modèle ML de prédiction
├── templates/              # HTML (Jinja2)
│   ├── login.html
│   ├── add_patient.html
│   ├── patients.html
├── static/                 # CSS (facultatif)
├── database.py             # Connexion PostgreSQL
├── schemas.py              # Pydantic models
└── utils.py                # Fonctions utilitaires (ex: prédiction, hashing)


# 10. 📎 Conclusion
Le projet DiabetoWeb est un exemple concret d’intégration de l’intelligence artificielle dans le domaine médical. Il met en avant :

La puissance des frameworks modernes comme FastAPI,

L’importance de la sécurité et de la structuration des données de santé,

Le potentiel du machine learning pour améliorer le diagnostic médical.

Ce projet peut servir de base à des solutions plus larges de e-santé au Maroc et ailleurs.