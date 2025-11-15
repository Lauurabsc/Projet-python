# Projet python - Implémentation simplifiée du jeu Blue Prince 

Ce projet consiste à programmer une version simplifiée du jeu **Blue Prince** en Python.
Il met en oeuvre : 
- la programmation orientée objet (POO)
- la gestion d’une interface graphique via **Pygame**
- la gestion procédurale et l’aléatoire 
- la gestion de ressources

## Objectif du projet

Le joueur explore un manoir généré pièce par pièce, en choisissant parmi trois salles proposées lorsqu’il ouvre une porte. Il doit atteindre l’**AnteChamber**, située tout en haut du manoir, sans épuiser des pas. 

## Fonctionnalités implémentées
Ce projet suit les exigences du *parcours IPS*.

### Mécaniques principales
- Déplacement dans le manoir
- Ouverture des portes selon leur niveau de vérrouillage (0, 1 ou 2)
- Tirage aléatoire de trois pièces lors de l’ouverture d’une porte
- Choix d’une pièce parmi les trois pièces proposées
- Gagne des pas avec de la nourriture
- Décompte des pas (-1 pas par déplacement)

### Fin de partie  
- Victoire : atteindre l’AnteChamber
- Défaite : nombre de pas épuisé ou impossibilité de progresser dans le manoir

### Gestion des ressources
- Ramassage et dépense de **gemmes** pour choisir une pièce
- Ramassage et dépense de **clés** pour ouvrir les portes
- Ramassage et dépense de **dés** pour relancer un tirage
- Système aléatoire dans : 
    - les pièces tirées, 
    - les objets disponibles dans les pièces 
    - le niveau de **verrouillage** des portes
- Prise en compte de la **rareté** des pièces (1, 2 ou 3)

## Inventaire 
### Objets consommables
- Pas
- Gemmes
- Clés
- Dés

### Objets permanents (+ effets associés)
- Détecteur de métaux
- Patte de lapin
- Kit de crochetage et ouverture des portes de niveau 1

## Structure du projet 

main.py --> Point d‘entrée du jeu

jeu.py --> Boucle principale Pygame et affichage, interactions

manoir.py --> Gestion de la grille

joueur.py --> Déplacements, inventaire et actions du joueur

Inventaire.py --> Gestion des ressources (pas, gemmes, clés, etc)

porte.py --> Classe Porte - gestion des niveaux de verrouillage

piece/piece.py --> Classe mère 

piece/piece_special.py --> Pièces spéciales (Entrance Hall et AnteChamber)

Autres pièces : 

piece/pieceorange.py 

piece/pieces_bleues.py

piece/pieceviolette.py

piece/pieces_rouges.py

piece/pieces_vertes.py

Images/ --> Ressources graphiques

README.md --> Documentation du projet

requirement.txt --> Listing des modules et bibliothèques nécessaires 

## Installation
pip install -r requirements.txt

## Lancement du jeu
Dans le terminal faire : python main.py
