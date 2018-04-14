# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import os
import easygui as eg

from GeStock_Users import *
from GeStock_HistoryIn import *
from GeStock_Stock import *
from GeStock_Sell import *
from GeStock_HistoryOut import *
from GeStock_Bonus import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def afficheMenu():
    listeActions = ["Vente","Ajouter Utilisateur","Crediter Utilisateur", "Consulter Utilisateur", "Ajouter Produit", "Ajouter Stock", "Consulter Stock", "Sauvegarder & Quitter"]
    data = eg.choicebox(msg="Que souhaitez vous faire ?", title="GeStock", choices=listeActions)
    launch(data)

#Vérification et création des tables
#Ne devrait être utile que lorsque que la BD à été corrompue
#TODO : Sauvegarde auto
initUsers()
initHistoryIn()
initStock()
initHistoryStock()
initHistoryOut()
initBonus()

def launch(rep):
    if rep == "Vente":
        vendre()
    elif rep == "Ajouter Utilisateur":
        ajouterUtilisateur()
    elif rep == "Crediter Utilisateur":
        crediterUtilisateur()
    elif rep == "Consulter Utilisateur":
        consulterSolde()
    elif rep == "Ajouter Produit":
        ajouterProduit()
    elif rep == "Ajouter Stock":
        ajouterStock()
    elif rep == "Consulter Stock":
        consulterStock()
    elif rep == "Transferer solde Bonus":
        transfererBonus()
    elif rep == "Sauvegarder & Quitter":
        c.close()
        exit()
    else:
        eg.msgbox(msg="Choix inconnu", title="Erreur !")
        time.sleep(2)

while 1:
    afficheMenu()
