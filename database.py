import sqlite3

def db():
    return sqlite3.connect("database.db")

def init():

    con=db()

    con.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    money INTEGER)
    """)

