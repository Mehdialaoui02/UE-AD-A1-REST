# UE-AD-A1-REST

# Gestion de Salle de Cinéma

Ce projet est une application de gestion de salle de cinéma, permettant la gestion des films, des séances, des réservations et des salles. 

## Fonctionnalités

- Gestion des films : Ajouter, modifier, supprimer des films
- Gestion des séances : Planifier les horaires et les salles
- Gestion des réservations : Réserver des places pour une séance

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé les éléments suivants :

- Python et Pip

## Installation et Lancement en Local

Suivez ces étapes pour configurer et lancer le projet en local.

1. **Clonez le dépôt**

   ```bash
   git clone https://github.com/Mehdialaoui02/UE-AD-A1-REST.git
   ```

2. **Installez les dépendanses**

    Assurez vous d'avoir python et pip installés sur votre machine puis lancez :
    ```bash
   pip install -r requirements.txt
   ```
3. **Lancez les serveur**

    Lancez chacune des commande dans un terminal différents :
   - Le serveur movie sur le port 3200
   ```bash 
    cd movie
    python movie.py 
   ``` 
    - Le serveur booking sur le port 3201
    ```bash 
    cd booking
    python booking.py 
   ```
   - Le serveur showtime sur le port 3202
   ```bash 
    cd showtime
    python showtime.py 
   ``` 
   - Le serveur user sur le port 3203
   ```bash 
    cd user
    python user.py 
   ```

