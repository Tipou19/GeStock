# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import os

from GeStock_Users import *
from GeStock_HistoryIn import *
from GeStock_Stock import *
from GeStock_Sell import *
from GeStock_HistoryOut import *
from GeStock_Bonus import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def afficheHeader():
    cls()
    for i in range(2): print(100*'#')
    print();print()
    print(46*' ', end='')
    print("GeStock \n")
    print(86*' ', end='')
    print("Nicolas PINHAL")
    for i in range(2): print(100*'#')

def afficheMenu():
    space=15
    print();print(space*' ', end='');print("1) Vente")
    print();print(space*' ', end='');print("2) Ajouter Utilisateur")
    print();print(space*' ', end='');print("3) Crediter Utilisateur")
    print();print(space*' ', end='');print("4) Consulter Solde")
    print();print(space*' ', end='');print("5) Ajouter Produit")
    print();print(space*' ', end='');print("6) Ajouter Stock")
    print();print(space*' ', end='');print("7) Consulter Stock")
    print();print(space*' ', end='');print("9) Sauvegarder & Quitter")

#Vérification et création des tables
#Ne devrait être utile que lorsque que la BD à été corrompue
#TODO : Sauvegarde auto
initUsers()
initHistoryIn()
initStock()
initHistoryStock()
initHistoryOut()

while 1:
    afficheHeader()
    afficheMenu()
    rep = input()
    if rep == "1":
        vendre()
    elif rep == "2":
        ajouterUtilisateur()
    elif rep == "3":
        crediterUtilisateur()
    elif rep == "4":
        consulterSolde()
    elif rep == "5":
        ajouterProduit()
    elif rep == "6":
        ajouterStock()
    elif rep == "7":
        consulterStock()
    elif rep == "9":
        c.close()
        exit()
    else:
        pass
    cls()


#ajouterUtilisateur()
#consulterSolde()
#crediterUtilisateur()

#ajouterProduit()
#ajouterStock()
#consulterStock()

#vendre()
