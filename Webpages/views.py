import sqlite3
from flask import Flask
from flask import render_template
from . import app

import os

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/portfolio")
def portfolio():
    if os.path.isfile("portfolio.db"):
        con = sqlite3.connect("portfolio.db")

    con.row_factory = sqlite3.Row

    cur = con.cursor()

    """
    #Print all from database to terminal
    cur.execute("select * from projects")
    rows = cur.fetchall()
    print(len(rows))
    for r in rows:
        print("Name: ",r[0])
        print("Type: ",r[1])
        print("url: ",r[2])
        print("desc: ",r[3])
        print("lang: ",r[4])
        print("\n")

    return render_template('home.html')
    """

    query = "select * from projects where type = ?"

    #Separate categories
    cur.execute(query, ("game",))
    gameRows = cur.fetchall() 

    cur.execute(query, ("app",))
    appRows = cur.fetchall()

    cur.execute(query, ("website",))
    websiteRows = cur.fetchall()

    cur.close()

    return render_template('portfolio.html', gameRows=gameRows, appRows=appRows, websiteRows=websiteRows)