# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
from GeStock_HistoryIn import *
from GeStock_HistoryStock import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def initHistoryStock():
        c.execute("CREATE TABLE IF NOT EXISTS historyOut (idCarte INTEGER, idProduit, timestamp VARCHAR)")
    

def historyStock(idProduit, stock):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M:%S'))
    c.execute("INSERT INTO historyStock (idProduit, stock, timestamp) VALUES (?, ?, ?)",
              (idProduit, stock, date))
    conn.commit()
    print("Ajout dans l'historique ... OK !")
    time.sleep(1)
