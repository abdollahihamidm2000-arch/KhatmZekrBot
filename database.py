import sqlite3

DB_NAME = "khadem.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        full_name TEXT,
        username TEXT,
        total_zikr INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS khatm(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        niat TEXT,
        zikr TEXT,
        minimum INTEGER,
        start_date TEXT,
        end_date TEXT,
        report_time TEXT,
        active INTEGER DEFAULT 1
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        khatm_id INTEGER,
        count INTEGER,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
