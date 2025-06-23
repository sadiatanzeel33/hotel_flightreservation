# db.py
import sqlite3
import pandas as pd

DB_NAME = "reservation.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            airline TEXT,
            flight_no TEXT,
            departure TEXT,
            arrival TEXT,
            dep_time TEXT,
            arr_time TEXT,
            ticket TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            hotel TEXT,
            room TEXT,
            checkin TEXT,
            checkout TEXT,
            res_no TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_flight(name, airline, flight_no, departure, arrival, dep_time, arr_time, ticket):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO flights VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", 
              (name, airline, flight_no, departure, arrival, dep_time, arr_time, ticket))
    conn.commit()
    conn.close()

def add_hotel(name, hotel, room, checkin, checkout, res_no):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO hotels VALUES (NULL, ?, ?, ?, ?, ?, ?)", 
              (name, hotel, room, checkin, checkout, res_no))
    conn.commit()
    conn.close()

def get_all_flights():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM flights", conn)
    conn.close()
    return df

def get_all_hotels():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM hotels", conn)
    conn.close()
    return df
