import sqlite3 as sql

conn = sql.connect("portfolio.db")

#conn.execute("CREATE TABLE projects (name TEXT, type TEXT, pic_url TEXT, description TEXT, language TEXT)")

cur = conn.cursor()
insert_query = "INSERT INTO projects (name,type,pic_url,description,language) VALUES (?,?,?,?,?)"

"""
cur.execute(insert_query, ("Swinglax","game","swinglax.png","Swing on a rope and dodge the falling objects. Grab power-ups and stay alive!","c++ (unity)"))
cur.execute(insert_query, ("Alarm Clock","website","alarm_clock.png","A website that combines an alarm and timer.","html, css, js"))
cur.execute(insert_query, ("Pizza Run","game","pizza_run.png","Don't get caught by the humans! Shoot them with pineapples before they get too close...","Python (PyGame)"))
cur.execute(insert_query, ("Pomodoro","app","pomodoro.png","Pomodoro Timer combined with a To-Do List. Perfect tool to help stay on track!","WPF"))
"""

cur.execute(insert_query, ("Expense Tracker","app","expense_tracker.png","An application to keep track of your expenses.", "WPF"))

conn.commit()

conn.close()