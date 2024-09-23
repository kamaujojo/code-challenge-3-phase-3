import sqlite3

def get_concerts_for_venue(venue_id, connection):
    query = """
    SELECT * FROM concerts WHERE venue_id = ?
    """
    cursor = connection.execute(query, (venue_id,))
    return cursor.fetchall()

def get_bands_for_venue(venue_id, connection):
    query = """
    SELECT DISTINCT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    """
    cursor = connection.execute(query, (venue_id,))
    return cursor.fetchall()

def get_concert_on_date(venue_id, date, connection):
    query = """
    SELECT * FROM concerts
    WHERE venue_id = ? AND date = ?
    LIMIT 1
    """
    cursor = connection.execute(query, (venue_id, date))
    return cursor.fetchone()