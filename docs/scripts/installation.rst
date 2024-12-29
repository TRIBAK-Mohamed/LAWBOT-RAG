Installation
============

Pour configurer **LAWBOT-RAG**, suivez ces étapes :

1. Clonez le dépôt GitHub : git clone https://github.com/TRIBAK-Mohamed/LAWBOT-RAG.git cd LAWBOT-RAG
2. Créez un environnement virtuel et activez-le : python -m venv env source env/bin/activate
3. Installez les dépendances : pip install -r requirements.txt
4. Configurez les variables d'environnement si nécessaire :
    - Ajoutez vos clés API dans un fichier `.env`.
5.  Lancez l’application :streamlit run llm_streamlit.py
### Préparation pour les documents utilisateur

Pour permettre aux utilisateurs d'importer leurs documents :
- Assurez-vous que les bibliothèques pour traiter les fichiers PDF et Word sont bien installées. 
- Exemple de configuration pour les dépendances : 
    - Pour les fichiers PDF : `pip install PyMuPDF`
    - Pour les fichiers Word : `pip install python-docx`
 Les documents acceptés sont :
- Fichiers PDF
- Documents Word (.docx)