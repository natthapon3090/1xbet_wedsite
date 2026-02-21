from flask import Flask,request,redirect,render_template_string,session
import sqlite3
import random

app=Flask(__name__)
app.secret_key="1234"

######## DATABASE ########

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

    con.execute("""
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    detail TEXT,
    image TEXT)
    """)

    con.execute("""
    CREATE TABLE IF NOT EXISTS chat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    msg TEXT)
    """)
