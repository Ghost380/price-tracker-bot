import sqlite3
from datetime import datetime
import os

DB_PATH = 'data/prices.db'

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            price REAL,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def log_price(name, price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO price_history (product_name, price, timestamp) VALUES (?, ?, ?)",
                   (name, price, datetime.now()))
    conn.commit()
    conn.close()

def get_lowest_price(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(price) FROM price_history WHERE product_name = ?", (name,))
    result = cursor.fetchone()[0]
    conn.close()
    return result if result else float('inf')