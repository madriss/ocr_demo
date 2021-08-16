Attention : cet outil a un but strictement démonstratif et ne doit pas être utilisé dans des conditions réelles

Pour lancer l'app streamlit en local : streamlit run infer.py

Spécificité à GCP, la commande devrait être la suivante : streamlit run --server.port 8080 --server.enableCORS false infer.py
