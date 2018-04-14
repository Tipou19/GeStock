# **GeStock**
Nicolas PINHAL

Tout droits réservés

Ce logiciel à été réalisé dans le but de gérer le stock de boissons et de snacks du BDE Informatique, les principaux objectifs étaient la légèreté, la portabilité ainsi que la facilité d'amélioration et d'entretient.
Vous ne pouvez pas modifier ou utiliser mon code sans mon autorisation préalable.

## Utilisation
**Sous Windows :**

 - Avoir Python3 installé
 - Avoir installé les librairies suivantes :
sqlite3,
time,
datetime,
random,
os .
- Lancer GeStock.ink
- EasyGui se charge automatique car il est inclus dans la source

**Sous Linux :**

 - Avoir Python3 installé
 - Avoir installé les librairies suivantes :
sqlite3,
time,
datetime,
random,
os .
- Lancer `python3 bin/GeStock.py`
- EasyGui se charge automatique car il est inclus dans la source

## Détails
**RFID :**
Ce soft a été créé pour être utilisé avec un lecteur de cartes RFID USB ( EM4100 125KHz ).

**Précisions importantes sur le lecteur :**

Le lecteur de cartes est considéré comme un clavier par l'os : il envoie un séquence de touches et fini par la touche entrée. Attention si le clavier n'est pas en majuscule le lecteur ne renverra pas des chiffres mais leurs symboles correspondant ( Uniquement sur clavier AZERTY sous windows )

**Visualisation de la BDD :**

La visualisation et/ou la modification de la BDD peut-être effectuée grâce à :

 - Un site web dédié à l'affichage et à la modification des stocks (**TODO**)
 - Un gestionnaire de BDD, je ne peut que conseiller DB Browser `http://sqlitebrowser.org/`

## TODO

 - Interface GUI **DONE**
 - Erreur de typage lors du credit d'un nombre à virgule **DONE**
 - Page web affichage stocks
