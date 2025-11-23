# fintrak_db.py - Original SQLite database initializer for FinTrak app

import sqlite3
from os import makedirs
from os.path import dirname, exists

DB_LOC = "data/fintrak_storage.db"

def connect_fintrak_db():
    """
    Establish a connection to the FinTrak SQLite database.
    Ensures the directory structure exists before connecting.
    """
    folder = dirname(DB_LOC)
    if not exists(folder):
        makedirs(folder)  # Create missing folders for DB path

    return sqlite3.connect(DB_LOC)

def setup_fintrak_db():
    """
    Create essential tables: ledger and targets for incomes/expenses and saving goal
    Applies data integrity constraints for realistic finance tracking.
    """
    conn = connect_fintrak_db()
    cur = conn.cursor()

    # Ledger stores all financial transactions with strict type and positive amounts
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ledger (
            entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_type TEXT NOT NULL CHECK(entry_type IN ('income','expense')),
            category TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount > 0),
            entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Single-row table for setting personal saving target, goal amount cannot be negative
    cur.execute("""
        CREATE TABLE IF NOT EXISTS targets (
            id INTEGER PRIMARY KEY CHECK(id = 1),
            saving_goal REAL NOT NULL CHECK(saving_goal >= 0)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_fintrak_db()
    print("FinTrak database initialized successfully!")
