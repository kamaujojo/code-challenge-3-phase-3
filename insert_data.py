import sqlite3

def insert_data():
    # Connect to SQLite3 database
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")

    # Insert sample data into bands table
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('The Beatles', 'Liverpool')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Pink Floyd', 'London')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Led Zeppelin', 'London')")

    cursor.execute("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('The O2 Arena', 'London')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Hollywood Bowl', 'Los Angeles')")

    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-09-15')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-10-12')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (3, 3, '2024-11-22')")

    # Commit the insertions
    connection.commit()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    insert_data()
