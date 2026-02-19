import sqlite3
import os

DB_PATH = "data/app.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mode TEXT,
        wallet_balance REAL,
        spend_limit REAL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        item TEXT,
        price REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_order(user_name, item, price):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO orders (user_name, item, price, status) VALUES (?, ?, ?, ?)",
              (user_name, item, price, "Placed"))
    conn.commit()
    conn.close()

def get_orders(user_name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT item, price, status FROM orders WHERE user_name = ?", (user_name,))
    data = c.fetchall()
    conn.close()
    return data