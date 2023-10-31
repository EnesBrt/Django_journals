
# My journal

## Description du Projet
Django_journals est un blog personnel développé en utilisant le framework Django. Ce projet est conçu pour être une plateforme où je peux partager mes pensées, travaux et projets avec une audience plus large.

## Fonctionnalités Principales
- **Blog Personnel**: Un espace pour publier et gérer des articles de blog.
- **Formulaire de Contact**: Une fonctionnalité récemment ajoutée pour permettre aux visiteurs de prendre contact.

## Installation
Pour installer et configurer ce projet, suivez les étapes ci-dessous :

1. **Prérequis** : Assurez-vous d'avoir Python et pip installés sur votre système.
2. **Environnement Virtuel** : Créez un environnement virtuel pour gérer les dépendances.
   ```
   python -m venv monenv
   source monenv/bin/activate  # Sur Windows utilisez `monenv\Scripts\activate`
   ```
3. **Installation de Django et Dépendances** :
   ```
   pip install django
   pip install -r requirements.txt  # Si un fichier requirements.txt est fourni
   ```

## Run
Pour lancer le projet, suivez ces étapes :

1. **Base de Données** : Configurez votre base de données en modifiant les paramètres dans `settings.py`.
2. **Migrations** : Appliquez les migrations pour préparer la base de données.
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Serveur de Développement** : Lancez le serveur de développement local.
   ```
   python manage.py runserver
   ```

## Introduction aux Paramètres des Fonctionnalités Principales
Dans `settings.py`, vous trouverez toutes les configurations nécessaires pour personnaliser les fonctionnalités principales du blog, telles que les paramètres de la base de données et les réglages du formulaire de contact.

## Fonctionnalité Email
Pour configurer la fonctionnalité d'envoi d'email, vous devez définir les paramètres suivants dans `settings.py` :

- `EMAIL_HOST`: Le serveur d'envoi de votre fournisseur d'email.
- `EMAIL_PORT`: Le port utilisé par le serveur d'email.
- `EMAIL_HOST_USER`: Votre adresse email.
- `EMAIL_HOST_PASSWORD`: Le mot de passe de votre adresse email.
- `EMAIL_USE_TLS`: Sécurisation de la connexion au serveur d'email.

N'oubliez pas de remplacer ces valeurs par vos informations personnelles pour que la fonctionnalité de messagerie fonctionne correctement.

## Screenshots

![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.27.18.png)
![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.27.33.png)
![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.27.43.png)
![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.27.54.png)
![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.28.13.png)
![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.32.10.png)
![](https://raw.githubusercontent.com/EnesBrt/Django_journals/main/Pictures/Capture%20d’écran%202023-10-31%20à%2012.31.14.png)



