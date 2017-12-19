#-*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
from GeStock_HistoryIn import *
from GeStock_HistoryStock import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def initStock():
    c.execute("CREATE TABLE IF NOT EXISTS stock (idProduit INTEGER, desc VARCHAR, prix REAL, stock INTEGER )")

def ajouterProduit():
    c.execute ('SELECT COUNT(*) FROM stock')
    data = c.fetchone()
    idProduit = data[0]+1
    desc = str(input("Entrez le nom du produit : "))
    prix = input(str("Entrez le prix : "))
    stock = input(str("Combien de stock ? : "))
    
    c.execute("INSERT INTO stock (idProduit, desc, prix, stock) VALUES ( ?, ?, ?, ?)",
        (idProduit, desc, prix, stock))
    conn.commit()
    print("Produit ajouté !")
    historyStock(idProduit, stock)

def ajouterStock():
    rep = "n"
    while rep == "n":
        idProduit = input("Quel est l'ID produit Ã  restocker ? : ")
        c.execute ('SELECT count(*) FROM stock WHERE idProduit = '+ idProduit)
        count = c.fetchone()
        if count[0] == 1:
            c.execute ('SELECT desc FROM stock WHERE idProduit = '+ idProduit)
            desc = c.fetchone()
            print("Voulez vous restocker du ", desc[0] ," ? ( Y / N || O / N )")
            rep = input()

        else:
            print("Impossible de trouver un produit avec cet ID ...")

    c.execute ('SELECT stock FROM stock WHERE idProduit = '+ idProduit)
    stock = c.fetchone()
    stock = stock[0]
    rajout = int(input("Combien de stock Ã  rajouter ? "))
    stock += rajout
    stock = str(stock)
    c.execute("UPDATE stock SET stock = " + stock + "  WHERE idProduit = " +idProduit)
    conn.commit()
    historyStock(idProduit, rajout)
	
def consulterStock():
    c.execute("SELECT desc, stock FROM stock")
    for row in c.fetchall():
        print(row)
    wait = input("Appuyer sur n'importe quelle touche pour continuer ...")
