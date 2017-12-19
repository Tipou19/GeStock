# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import easygui as eg
from GeStock_HistoryIn import *
from GeStock_Bonus import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def initUsers():
    c.execute("CREATE TABLE IF NOT EXISTS users (idCarte INTEGER, solde REAL, nom VARCHAR)")

def tradCarte(temp):
    res = []
    resInt = 0
    for i in range(len(temp)):
        if temp[i] == "&" or temp[i] == "1":
            res.append(1)
        elif temp[i] == "é" or temp[i] == "2":
            res.append(2)
        elif temp[i] == '"' or temp[i] == "3":
            res.append(3)
        elif temp[i] == "'" or temp[i] == "4":
            res.append(4)
        elif temp[i] == "(" or temp[i] == "5":
            res.append(5)
        elif temp[i] == "-" or temp[i] == "6":
            res.append(6)
        elif temp[i] == "è" or temp[i] == "7":
            res.append(7)
        elif temp[i] == "_" or temp[i] == "8":
            res.append(8)
        elif temp[i] == "ç" or temp[i] == "9":
            res.append(9)
        elif temp[i] == "à" or temp[i] == "0":
            res.append(0)
        else:
            res.append(temp[i])
    for i in range(len(res)):
        resInt += res[len(res)-i-1]*10**i
    return(resInt)

def ajouterUtilisateur():
    temp = eg.enterbox(msg="Passez une carte vierge")
    carte = str(tradCarte(temp))
    c.execute ('SELECT COUNT(idCarte) FROM users WHERE idCarte = '+ carte)
    count = c.fetchone()
    if count[0] > 0 :
        eg.msgbox(msg="Il y a déjà un utilisateur enregistré sur cette carte !")
    else:
        nom = eg.enterbox(msg="Nom de l'utilisateur",title="Enregistrement")
        solde = eg.enterbox(msg="Solde de l'utilisateur",title="Enregistrement")
        c.execute("INSERT INTO users (idCarte, solde, nom) VALUES ( ?, ?, ?)",
              (carte, solde, nom))
        conn.commit()
        eg.msgbox(msg="Utilisateur ajouté !", title="Succès !")
        historyIn(carte, solde)
        time.sleep(1)

def consulterSolde():
    temp = eg.enterbox(msg="Passez une carte ...")
    carte = str(tradCarte(temp))
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)
    solde = c.fetchone()
    solde = "Le solde est de : ", solde[0] ," E"
    solde = beautify(solde)
    eg.msgbox(msg=solde, title='Solde')
    time.sleep(2)

def crediterUtilisateur():
    temp = eg.enterbox(msg="Passez une carte ...")
    carte = str(tradCarte(temp))
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)
    solde = c.fetchone()
    solde=("Le solde est de : ", solde[0]," E")
    solde=beautify(solde)
    credit= int(eg.enterbox(msg="Combien à crediter ?"))
    historyIn(carte, credit)
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)
    solde = c.fetchone()
    credit += solde[0]
    credit = str(credit)
    c.execute("UPDATE users SET solde = " + credit + "  WHERE idCarte = " +carte)
    conn.commit()
    total = "Le credit est à présent de : ", credit
    total= beautify(total)
    eg.msgbox(msg=total, title="Mise a jour")
    time.sleep(1)
