# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
from GeStock_HistoryIn import *

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
    print("Conversion, OK !", resInt)
    return(resInt)

def ajouterUtilisateur():
    print("Ajout d'un utilisateur, préparez la carte")
    print("Passez la carte")
    temp = str(input())
    carte = str(tradCarte(temp))
    c.execute ('SELECT COUNT(idCarte) FROM users WHERE idCarte = '+ carte)
    count = c.fetchone()
    if count[0] > 0 :
        print("Il y a déjà un utilisateur enregistré sur cette carte !")
    else:
        nom = input("Entrez le nom du propriétaire : ")
        solde = input("Entrez le solde : ")
        c.execute("INSERT INTO users (idCarte, solde, nom) VALUES ( ?, ?, ?)",
              (carte, solde, nom))
        conn.commit()
        print("Utilisateur ajouté !")
        historyIn(carte, solde)
        time.sleep(1)

def consulterSolde():
    temp = str(input("Passez la carte \n"))
    carte = str(tradCarte(temp))
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)
    solde = c.fetchone()
    print("Le solde est de : ", solde[0]," E")
    time.sleep(2)

def crediterUtilisateur():
    temp = str(input("Passez la carte \n"))
    carte = str(tradCarte(temp))
    c.execute ('SELECT solde FROM users WHERE idCarte = '+ carte)
    solde = c.fetchone()
    print("Le solde est de : ", solde[0]," €")
    credit= int(input("Combien d'€ à crediter ? : "))
    historyIn(carte, credit)
    credit += solde[0]
    credit = str(credit)
    c.execute("UPDATE users SET solde = " + credit + "  WHERE idCarte = " +carte)
    conn.commit()
    print("Le credit est à présent de : ", credit)
    time.sleep(1)
        
