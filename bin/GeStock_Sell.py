# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
from GeStock_Users import *
from GeStock_HistoryIn import *
from GeStock_Stock import *
from GeStock_HistoryOut import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def vendre():
    rep = "n"
    while rep == "n":
        idProduit = input("Quel est l'ID produit à vendre ? : ")
        c.execute ('SELECT stock FROM stock WHERE idProduit = '+ idProduit)
        count = c.fetchone()
        count = count[0]
        print("Count ", count)
        if count > 0:
            c.execute ('SELECT desc FROM stock WHERE idProduit = '+ idProduit)
            desc = c.fetchone()
            print("Voulez vous vendre du ", desc[0] ," ? ( Y / N || O / N )")
            rep = input()

        else:
            print("ID invalide ou stock nul")

    debiter(idProduit, count)

def debiter(idProduit, count):
    #Récupération du prix
    c.execute ('SELECT prix FROM stock WHERE idProduit = '+ idProduit)
    prix = c.fetchone()
    prix = prix[0]
    #Affichage du prix + Récuperation de la carte
    print("A payer", prix ,"Passez la carte")
    temp = str(input())
    carte = str(tradCarte(temp))
    #Debit
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)    
    solde = c.fetchone()
    solde = solde[0]    
    if solde > prix :
        c.execute("UPDATE users SET solde = " + str(solde - prix) + "  WHERE idCarte = " + str(carte))
        print("Debit ... OK !")
        deb = str(count - 1)
        prod = str(idProduit)
        c.execute("UPDATE stock SET stock = " + deb + " WHERE idProduit = " + prod)
        print("Destockage ... OK !")
        conn.commit()
        historyOut(carte, idProduit)
    else:
        print("Sold INSUFISANT   ", solde)


    
