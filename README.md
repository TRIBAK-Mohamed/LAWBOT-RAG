##LawBot - Chatbot Juridique
LawBot est une application alimentée par l'IA conçue pour fournir des informations juridiques sur le droit de la famille marocain et d'autres domaines juridiques. Ce projet combine des techniques de traitement du langage naturel (NLP), la recherche vectorielle et une interface utilisateur intuitive via Streamlit.
Fonctionnalités
Extraction et ingestion de documents : Traite des fichiers PDF et extrait leur contenu pour l'intégrer dans une base de données vectorielle.
Recherche contextuelle : Utilise une recherche vectorielle pour répondre précisément aux questions basées sur les documents chargés.
Chat interactif : Répond aux questions générales ou spécifiques sur les documents chargés.
Support du droit marocain : Spécifiquement conçu pour répondre aux questions liées au droit de la famille marocain.
Prérequis
Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

Python 3.9 ou supérieur
LangChain
Streamlit
pdfplumber
Les dépendances nécessaires sont définies dans le fichier requirements.txt.
Utilisation
Étape 1 : Indexation des documents
Ajoutez vos fichiers PDF dans le dossier documents.
Lancez le script pour ingérer les documents dans la base de données vectorielle :
bash
Copier le code
python pdf.py
Étape 2 : Interaction via Streamlit
Lancez l'application Streamlit :

bash
Copier le code
streamlit run llm_streamlit.py
Accédez à l'application via le navigateur à l'adresse suivante :

arduino
Copier le code
http://localhost:8501
Fonctionnalités disponibles :

Téléchargez un fichier PDF et posez des questions directement sur son contenu.
Posez des questions générales sans document.

Voici une suggestion pour le contenu de votre fichier README.md adapté à votre projet :

LawBot - Chatbot Juridique
LawBot est une application alimentée par l'IA conçue pour fournir des informations juridiques sur le droit de la famille marocain et d'autres domaines juridiques. Ce projet combine des techniques de traitement du langage naturel (NLP), la recherche vectorielle et une interface utilisateur intuitive via Streamlit.

Fonctionnalités
Extraction et ingestion de documents : Traite des fichiers PDF et extrait leur contenu pour l'intégrer dans une base de données vectorielle.
Recherche contextuelle : Utilise une recherche vectorielle pour répondre précisément aux questions basées sur les documents chargés.
Chat interactif : Répond aux questions générales ou spécifiques sur les documents chargés.
Support du droit marocain : Spécifiquement conçu pour répondre aux questions liées au droit de la famille marocain.
Prérequis
Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

Python 
LangChain
Streamlit
pdfplumber
Les dépendances nécessaires sont définies dans le fichier requirements.txt.

Installation
Clonez ce dépôt :


Copier le code
git clone <URL_du_dépôt>
cd LawBot
Installez les dépendances :


Copier le code
pip install -r requirements.txt
Configurez l'environnement virtuel :


Copier le code
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
Créez un fichier .env pour vos clés API et autres configurations :

plaintext
Copier le code
EMBEDDING_MODEL="mxbai-embed-large:latest"
CHAT_MODEL="llama3.2"
Utilisation
#Étape 1 : Indexation des documents
Ajoutez vos fichiers PDF dans le dossier documents.
Lancez le script pour ingérer les documents dans la base de données vectorielle :

Copier le code
python pdf.py
#Étape 2 : Interaction via Streamlit
Lancez l'application Streamlit :


Copier le code
streamlit run llm_streamlit.py
Accédez à l'application via le navigateur à l'adresse suivante :

Fonctionnalités disponibles :

Téléchargez un fichier PDF et posez des questions directement sur son contenu.
Posez des questions générales sans document.

Structure du projet

Copier le code
LawBot/
│
├── documents/            # Fichiers PDF à traiter
├── lawbot_DB/            # Base de données vectorielle persistée
├── llm_streamlit.py      # Interface utilisateur Streamlit
├── pdf.py                # Script pour l'ingestion des documents
├── requirements.txt      # Dépendances du projet
├── .env                  # Configuration de l'environnement
└── README.md             # Ce fichier


