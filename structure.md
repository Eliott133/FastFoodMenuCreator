```
FastFoodMenuCreator/
│
├── backend/                   # Dossier pour l'application Flask
│   ├── app/                   # Contient les modules de l'application
│   │   ├── __init__.py        # Point d'entrée de l'application
│   │   ├── models.py          # Modèles de base de données
│   │   ├── auth.py            # Routes d'authentification
│   │   ├── main.py            # Routes principales
│   │   ├── config.py          # Configuration de l'application
│   ├── db/                    # Dossier pour la base de données
│   │   ├── initDatabase.sql   # Fichier d'initialisation de la base de données 
│   ├── requirements.txt       # Dépendances Python
│
├── frontend/                  # Dossier pour l'application React
│   ├── public/                # Dossier pour les fichiers publics
│   ├── src/                   # Dossier source de l'application React
│   │   ├── components/        # Composants React
│   │   ├── pages/             # Pages de l'application (login, signup, etc.)
│   │   ├── App.jsx            # Composant principal
│   │   ├── App.css            # Css générale de l'application
│   │   ├── main.jsx           # Point d'entrée de l'application React
│   │   ├── index.html         # 
│   │   └── services/          # Services pour interagir avec le backend (API calls)
│   ├── package.json           # Dépendances React
│  
└── README.md                  # Documentation du projet
```