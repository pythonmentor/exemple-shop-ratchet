# Exemple de page produits

Pour tester cet exemple, il est nécessaire d'installer pipenv avec `pip install pipenv`, puis de 
suivre la procédure suivante:

1. Cloner ce dépôt de code avec git ou [télécharger l'archive zip](https://github.com/pythonmentor/exemple-shop-ratchet/archive/refs/heads/main.zip) et la décompresser sur votre ordinateur
2. Ouvrir un terminal à la racine du projet
3. Installer les dépendances avec `pipenv install --python 3.10` (adapter selon votre version de Python)
4. Activer l'environnement virtuel avec `pipenv shell`
5. Exécuter les migrations avec `python manage.py migrate`
6. Lancer le serveur de développement avec `python manage.py runserver`
7. Visiter la page d'accueil du site sur http://localhost:8000