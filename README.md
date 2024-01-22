# Projet Multithreading

Ce projet a été créé dans le cadre du cours de multithreading. Il est composé de différentes classes Python et d'un fichier C++ avec son propre CMakeLists.

## Classes Python

1. **Boss**
   - La classe Boss ajoute x Task de taille modifiable (4000 par défaut) dans une QueueClient (Managers).

2. **Managers**
   - La classe Managers utilise la QueueClient pour gérer les Task et les résultats.

3. **Minion**
   - La classe Minion traite les Task présentes dans la QueueClient.

4. **Proxy**
   - La classe Proxy permet d'envoyer un fichier JSON correspondant à la Task à traiter sur une adresse locale.

5. **Task**
   - La classe Task représente une résolution linéaire ax = b. Elle possède une fonction pour calculer le temps de résolution et résoudre l'équation. De plus, la classe Task peut convertir les paramètres liés à la Task au format JSON.

## Fichiers C++

Le projet comprend également un fichier CMakeLists et une classe C++.

1. **low_level**
   - La classe low_level permet la lecture d'un fichier JSON sur une adresse locale et la résolution de l'équation en fonction de la méthode choisie.

## Résultats

Le projet vise à démontrer l'utilisation du multithreading dans la résolution d'équations linéaires, en utilisant différentes classes Python pour gérer les tâches et un composant C++ pour la résolution bas niveau.

Pour une taille de matrice de 4000, j'obtiens les résultats suivants :

- Environ 9.8 secondes pour la résolution en Python.
- Environ 13.2 secondes avec la fonction colPivHouseholderQr en C++.
- Environ 1.9 secondes avec la fonction lu en C++.

Ces résultats sont obtenus sur ma machine et peuvent différer.
