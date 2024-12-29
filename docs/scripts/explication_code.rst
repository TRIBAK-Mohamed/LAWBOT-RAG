Explication des Parties du Code
===============================
Description  des différentes parties du projet et  leur rôle :

1. **`pdf.py` : Gestion des documents PDF**
   Ce fichier contient les fonctions nécessaires pour extraire et diviser le contenu des fichiers PDF avant de les indexer dans une base vectorielle.

   - **`read_pdf(file_path)`** :
     - Fonction : Lit un fichier PDF et extrait tout le texte.
     - Entrée : Chemin vers un fichier PDF.
     - Sortie : Texte brut extrait du PDF.

   

   - **`split_documents(documents)`** :
     - Fonction : Divise un document volumineux en petits morceaux pour améliorer la recherche vectorielle.
     - Entrée : Liste de documents.
     - Sortie : Liste de fragments de texte.

   - **`ingest_into_vector_store(documents)`** :
     - Fonction : Ajoute les documents extraits dans une base vectorielle (Chroma).
     - Entrée : Liste de fragments de documents.
     - Sortie : Base vectorielle persistante.

2. **`llm_streamlit.py` : Interface utilisateur Streamlit**
   Ce fichier fournit une interface utilisateur simple via Streamlit pour interagir avec le chatbot.

   - **Sections principales :**
     - **Téléchargement de fichiers PDF** :
       - L'utilisateur peut téléverser un fichier PDF contenant du texte juridique.
     - **Pose de questions générales** :
       - L'utilisateur peut poser des questions sans téléverser de fichier.
     - **Historique des conversations** :
       - Les interactions utilisateur sont affichées dans une section "Historique".
3. **`Fonctions communes` :**
 - **`initialize_vector_store()`** :
     - Fonction : Initialise la base vectorielle persistante pour la recherche.
     - Entrée : Appelée avant d'effectuer une recherche.
     - Sortie : Instance de la base Chroma.

   - **`retrieve_from_db(question)`** :
     - Fonction : Récupère les réponses les plus pertinentes dans la base vectorielle.
     - Entrée : Une question posée par l'utilisateur.
     - Sortie : Réponse générée par le modèle.