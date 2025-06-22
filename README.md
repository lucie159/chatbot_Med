# Chatbot Médical Vocal – FastAPI 

Ce projet implémente un **assistant médical vocal intelligent** en utilisant une architecture modulaire basée sur des microservices. Il permet à un patient de parler via une interface, recevoir une réponse médicale générée par IA, puis l’écouter sous forme audio synthétisée.

---

##  Fonctionnalités principales

-  **Reconnaissance vocale (STT)** avec Whisper
-  **Génération de réponse médicale** via un modèle LLM (GPT/HuggingFace)
-  **Synthèse vocale (TTS)** avec gTTS
-  **Filtrage du bruit** et détection de la voix (VAD)
-  Interface web simple (HTML/JS)
-  API backend FastAPI, Dockerisée

---

##  Architecture (Microservices)

```
[Utilisateur] → [Frontend] → [API Gateway] → [VAD] → [Denoise] → [STT] → [NLP/LLM] → [TTS] → [Frontend → Audio]
```

Chaque étape est gérée par un microservice indépendant dans le backend.

---

##  Structure du projet

```
chatbot_app/
├── frontend/
│   └── index.html               # Interface utilisateur
├── models/
│   └── init_model.py            # Initialisation LLM
├── routers/
│   └── voice_chat.py            # Route FastAPI principale
├── services/
│   ├── gpt_service.py           # NLP/LLM service
│   ├── stt_service.py           # Speech-to-text service
│   └── tts_service.py           # Text-to-speech service
├── main.py                      # Entrée FastAPI
├── req.txt                      # Dépendances Python
├── Dockerfile                   # Conteneurisation
├── .gitignore
└── README.md
```

---

##  Installation locale

### 1. Cloner le repo

```bash
git clone https://github.com/<ton_nom>/chatbot_med.git
cd chatbot_med
```

### 2. Créer un environnement Python

```bash
python -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate sous Windows
pip install -r req.txt
```

### 3. Lancer l’API FastAPI

```bash
uvicorn main:app --reload
```

---

##  Exécution avec Docker

### 1. Build de l’image

```bash
docker build -t chatbot-med .
```

### 2. Exécuter le conteneur

```bash
docker run -p 8000:8000 chatbot-med
```

---

##  Accès

- Interface frontend : [http://localhost:8000](http://localhost:8000)
- Docs API Swagger : [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Prérequis

- Python 3.10+
- pip
- Docker (optionnel)

---

##  Licence

Projet sous licence MIT. Utilisation à des fins éducatives encouragée.

---

##  Contribuer

Les PRs sont les bienvenues. Merci de proposer des améliorations ou correctifs !
