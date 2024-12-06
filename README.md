# LawBot - Chatbot Juridique

**LawBot** est une application alimentée par l'IA conçue pour fournir des informations juridiques sur le droit de la famille marocain et d'autres domaines juridiques. Ce projet combine des techniques de traitement du langage naturel (**NLP**), la recherche vectorielle et une interface utilisateur intuitive via **Streamlit**.

---

## ✨ Fonctionnalités

- **Extraction et ingestion de documents** :  
  Traite des fichiers PDF et extrait leur contenu pour l'intégrer dans une base de données vectorielle.
  
- **Recherche contextuelle** :  
  Utilise une recherche vectorielle pour répondre précisément aux questions basées sur les documents chargés.
  
- **Chat interactif** :  
  Répond aux questions générales ou spécifiques sur les documents chargés.
  
- **Support du droit marocain** :  
  Spécifiquement conçu pour répondre aux questions liées au droit de la famille marocain.

---

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

- Python 3.9 ou supérieur
- [LangChain](https://docs.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

Les dépendances nécessaires sont définies dans le fichier `requirements.txt`.

---

## ⚙️ Installation

1. **Clonez ce dépôt** :
   git clone <URL_DU_DÉPÔT>
   cd LawBot
2. **Installez les dépendances** :
   pip install -r requirements.txt
3. **Configurez l'environnement virtuel** :
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
## 🚀 Utilisation

### Étape 1 : Indexation des documents
1. Ajoutez vos fichiers PDF dans le dossier `documents`.
2. Lancez le script pour ingérer les documents dans la base de données vectorielle :
   python pdf.py
### Étape 2 : Interaction via Streamlit
Lancez l'application Streamlit :
   streamlit run llm_streamlit.py
### Fonctionnalités disponibles :
Téléchargez un fichier PDF et posez des questions directement sur son contenu.
Posez des questions générales sans document.
## 📂 Structure du projet
LawBot/
│
├── documents/            # Fichiers PDF à traiter
├── lawbot_DB/            # Base de données vectorielle persistée
├── llm_streamlit.py      # Interface utilisateur Streamlit
├── pdf.py                # Script pour l'ingestion des documents
├── requirements.txt      # Dépendances du projet
├── .env                  # Configuration de l'environnement
└── README.md             # Ce fichier
