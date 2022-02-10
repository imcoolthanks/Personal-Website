import sqlite3 as sql

conn = sql.connect("database.db")

conn.execute("CREATE TABLE projects (name TEXT, type TEXT, description TEXT, language TEXT, repo TEXT, devpost TEXT, link TEXT)")

cur = conn.cursor()
insert_query = "INSERT INTO projects (name,type, description,language,repo,devpost,link) VALUES (?,?,?,?,?,?,?)"

cur.execute(insert_query, ("Swinglax","game","Swing on a rope and dodge the falling objects. Grab power-ups and stay alive!","c++ (unity)",None,None,None))
cur.execute(insert_query, ("Alarm Clock","website","A website that combines an alarm and timer.","html, css, js","https://github.com/imcoolthanks/Alarm-Clock",None,None))
cur.execute(insert_query, ("Pizza Run","game","Don't get caught by the humans! Shoot them with pineapples before they get too close...","Python (PyGame)",None,None,None))
cur.execute(insert_query, ("Pomodoro","app","Pomodoro Timer combined with a To-Do List. Perfect tool to help stay on track!","WPF",None,None,None))

cur.execute(insert_query, ("Expense Tracker","app","An application to keep track of your expenses.", "WPF",None,None,None))

cur.execute(insert_query, ("BuildingTuition (StarHacks)","hackathon"," Web based app that has the ability to give students all the information they need about scholarships and bursaries.", "Flask, Jinja, SQLite, Twilio","https://github.com/otrachea/building-tuition","https://devpost.com/software/buildingtuition",None))

cur.execute(insert_query, ("Perplexio (JigsawHacks)","hackathon","Website with two integrated Unity puzzle games, fully supported by browsers", "Unity, C#, Web development (JS, HTML, CSS), itch.io","https://github.com/thinkingjet/Perplexio", "https://devpost.com/software/perplexio","https://perplexio.co/"))

cur.execute(insert_query, ("Rethinkably (Hack Your Tomorrow)","hackathon","""Rethinkkably.co matches an individual with another individual or organization that is in need of food
                            , clothing, or blood. Individuals can donate their resources to this local group, which makes the process smoother for all parties."""
                            , "React.js, Bootstrap5, Figma","https://github.com/thinkingjet/PTC","https://devpost.com/software/rethinkably-co","https://change-lives.netlify.app/"))

conn.commit()

conn.close()