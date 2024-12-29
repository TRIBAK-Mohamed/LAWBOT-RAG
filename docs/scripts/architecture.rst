Architecture
============

Le projet est structuré comme suit :

- **llm_streamlit.py** : Interface utilisateur avec Streamlit.
- **pdf.py** : Gestion et ingestion des documents PDF.
- **lawbot_DB/** : Stockage des embeddings vectoriels.
- **docs/** : Documentation pour ReadTheDocs.

**Schéma du workflow :**

1. Les documents PDF sont ingérés dans une base vectorielle via `pdf.py`.
2. Lorsqu'un utilisateur pose une question, le système recherche dans la base vectorielle pour trouver une réponse pertinente.
3. L'interface Streamlit affiche les réponses en temps réel.