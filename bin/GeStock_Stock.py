#-*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import easygui as eg
from GeStock_HistoryIn import *
from GeStock_HistoryStock import *
from GeStock_Users import *
from GeStock_Bonus import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def initStock():
    c.execute("CREATE TABLE IF NOT EXISTS stock (idProduit INTEGER, desc VARCHAR, prix REAL, stock INTEGER )")

def ajouterProduit():
    c.execute ('SELECT COUNT(*) FROM stock')
    data = c.fetchone()
    idProduit = data[0]+1
    desc = eg.enterbox(msg="Entrez le nom du produit : ",title="Ajout")
    prix = eg.enterbox(msg="Entrez le prix : ",title="Ajout")
    stock = eg.enterbox(msg="Combien de stock ? : ",title="Ajout")

    c.execute("INSERT INTO stock (idProduit, desc, prix, stock) VALUES ( ?, ?, ?, ?)",
        (idProduit, desc, prix, stock))
    conn.commit()
    eg.msgbox(msg="Produit ajouté !")
    historyStock(idProduit, stock)

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

def ajouterStock():
    rep = False
    while rep == False:
        idProduit = eg.enterbox(msg="Quel est l'ID produit Ã  restocker ? : ", title="idProduit")
        c.execute ('SELECT count(*) FROM stock WHERE idProduit = '+ idProduit)
        count = c.fetchone()
        if count[0] == 1:
            c.execute ('SELECT desc FROM stock WHERE idProduit = '+ idProduit)
            desc = c.fetchone()
            quest = "Voulez vous restocker du ", desc[0]," ?"
            quest = beautify(quest)
            rep = eg.ynbox(msg=quest)
        else:
            eg.msgbox(msg="Impossible de trouver un produit avec cet ID ...",title="Erreur")

    c.execute ('SELECT stock FROM stock WHERE idProduit = '+ idProduit)
    stock = c.fetchone()
    stock = stock[0]
    rajout = int(eg.enterbox(msg="Combien de stock Ã  rajouter ? ", title="Rajout"))
    stock += rajout
    stock = str(stock)
    c.execute("UPDATE stock SET stock = " + stock + "  WHERE idProduit = " +idProduit)
    conn.commit()
    historyStock(idProduit, rajout)

def consulterStock():
    c.execute("SELECT desc, stock FROM stock")
    total = ""
    for row in c.fetchall():
        temp = beautify(row)
        temp = temp + "\n"
        total+= temp
    eg.textbox(text=total, title="Stock")
