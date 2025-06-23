import streamlit as st
import sqlite3
import datetime

# ------------------ Database Setup ------------------
def init_db():
    conn = sqlite3.connect("reservations.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flight_reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    flight_number TEXT,
                    departure_datetime TEXT
                )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS hotel_reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    hotel_name TEXT,
                    checkin_datetime TEXT,
                    checkout_datetime TEXT
                )''')
    conn.commit()
    conn.close()

# ------------------ Insert Functions ------------------
def insert_flight(name, email, flight_number, departure_datetime):
    conn = sqlite3.connect("reservations.db")
    c = conn.cursor()
    c.execute("INSERT INTO flight_reservations (name, email, flight_number, departure_datetime) VALUES (?, ?, ?, ?)",
              (name, email, flight_number, departure_datetime))
    conn.commit()
    conn.close()

def insert_hotel(name, email, hotel_name, checkin_datetime, checkout_datetime):
    conn = sqlite3.connect("reservations.db")
    c = conn.cursor()
    c.execute("INSERT INTO hotel_reservations (name, email, hotel_name, checkin_datetime, checkout_datetime) VALUES (?, ?, ?, ?, ?)",
              (name, email, hotel_name, checkin_datetime, checkout_datetime))
    conn.commit()
    conn.close()

# ------------------ Main App ------------------
def main():
    st.set_page_config("🛫 Reservation System", layout="centered")
    st.title("🛫 Flight & 🏨 Hotel Reservation System")

    tab1, tab2, tab3 = st.tabs(["✈️ Flight", "🏨 Hotel", "📋 View Records"])

    with tab1:
        st.subheader("✈️ Flight Reservation")

        name = st.text_input("Full Name", key="f1")
        email = st.text_input("Email", key="f2")
        flight_number = st.text_input("Flight Number")

        dep_date = st.date_input("Departure Date", datetime.date.today())
        dep_time = st.time_input("Departure Time", datetime.datetime.now().time())
        dep_datetime = datetime.datetime.combine(dep_date, dep_time)

        if st.button("Submit Flight Reservation"):
            if name and flight_number:
                insert_flight(name, email, flight_number, dep_datetime.isoformat())
                st.success("✅ Flight reservation saved successfully.")
            else:
                st.warning("⚠️ Name and Flight Number are required.")

    with tab2:
        st.subheader("🏨 Hotel Reservation")

        name = st.text_input("Full Name", key="h1")
        email = st.text_input("Email", key="h2")
        hotel_name = st.text_input("Hotel Name")

        checkin_date = st.date_input("Check-in Date", key="c1")
        checkin_time = st.time_input("Check-in Time", key="c2")
        checkout_date = st.date_input("Check-out Date", key="c3")
        checkout_time = st.time_input("Check-out Time", key="c4")

        checkin_dt = datetime.datetime.combine(checkin_date, checkin_time)
        checkout_dt = datetime.datetime.combine(checkout_date, checkout_time)

        if st.button("Submit Hotel Reservation"):
            if name and hotel_name:
                insert_hotel(name, email, hotel_name, checkin_dt.isoformat(), checkout_dt.isoformat())
                st.success("✅ Hotel reservation saved successfully.")
            else:
                st.warning("⚠️ Name and Hotel Name are required.")

    with tab3:
        st.subheader("📋 All Reservations")

        with st.expander("✈️ View Flight Reservations"):
            conn = sqlite3.connect("reservations.db")
            c = conn.cursor()
            c.execute("SELECT name, email, flight_number, departure_datetime FROM flight_reservations")
            data = c.fetchall()
            for row in data:
                st.write(f"👤 {row[0]} | ✉️ {row[1]} | ✈️ {row[2]} | 🕒 {row[3]}")

        with st.expander("🏨 View Hotel Reservations"):
            c.execute("SELECT name, email, hotel_name, checkin_datetime, checkout_datetime FROM hotel_reservations")
            data = c.fetchall()
            conn.close()
            for row in data:
                st.write(f"👤 {row[0]} | ✉️ {row[1]} | 🏨 {row[2]} | 🟢 Check-in: {row[3]} | 🔴 Check-out: {row[4]}")

# ------------------ Run ------------------
if __name__ == "__main__":
    init_db()
    main()
