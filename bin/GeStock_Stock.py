#-*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import easygui as eg
from GeStock_HistoryIn import *
from GeStock_HistoryStock import *
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
