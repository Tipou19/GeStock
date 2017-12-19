# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import easygui as eg
from GeStock_Users import *
from GeStock_HistoryIn import *
from GeStock_Stock import *
from GeStock_HistoryOut import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def vendre():
    rep = False
    while rep == False:
        idProduit = eg.enterbox(msg="Quel est l'id du Produit ?",title="Vente !")
        if idProduit == None or idProduit == "":
            return
        c.execute ('SELECT stock FROM stock WHERE idProduit = '+ idProduit)
        count = c.fetchone()

        if count is None:
            eg.msgbox("ID invalide")
        else :
            count = count[0]
            if count == 0:
                eg.msgbox("Stock nul")
            else:
                c.execute ('SELECT desc FROM stock WHERE idProduit = '+ idProduit)
                desc = c.fetchone()
                msg = ("Voulez vous vendre du ", desc[0] ," ?")
                msg = beautify(msg)
                rep = eg.ynbox(msg = msg)

    debiter(idProduit, count)

def debiter(idProduit, count):
    #Récupération du prix
    c.execute ('SELECT prix FROM stock WHERE idProduit = '+ idProduit)
    prix = c.fetchone()
    prix = prix[0]
    #Affichage du prix + Récuperation de la carte
    paye = ("A payer ", prix ," Passez la carte")
    paye = beautify(paye)
    temp = eg.enterbox(msg=paye , title="Payement !")
    carte = str(tradCarte(temp))
    #Debit
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)
    solde = c.fetchone()
    solde = solde[0]
    if solde > prix :
        c.execute("UPDATE users SET solde = " + str(solde - prix) + "  WHERE idCarte = " + str(carte))
        c.execute("SELECT nom FROM users WHERE idCarte = "+ str(carte))
        compte = c.fetchone()
        debitMessage = ("Debit sur le compte \"", compte[0] , "\" ... OK !")
        deb = str(count - 1)
        prod = str(idProduit)
        c.execute("UPDATE stock SET stock = " + deb + " WHERE idProduit = " + prod)
        debitMessage = beautify(debitMessage)
        debitMessage += "\nDestockage ... OK !"
        c.execute("SELECT solde FROM users WHERE idCarte = "+ carte)
        solde = c.fetchone()
        debitMessage = (debitMessage, "\nSolde restant pour", compte[0] ," : ",solde[0])
        debitMessage = beautify(debitMessage)
        eg.msgbox(msg=debitMessage, title="Succès !")
        conn.commit()
        historyOut(carte, idProduit)
    else:
        eg.msgbox(msg="Solde INSUFISANT !!",title="Solde INSUFISANT !")
