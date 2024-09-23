import sqlite3

def get_concerts_for_band(band_id, connection):
    query = """
    SELECT * FROM concerts WHERE band_id = ?
    """
    cursor = connection.execute(query, (band_id,))
    return cursor.fetchall()

def get_venues_for_band(band_id, connection):
    query = """
    SELECT DISTINCT venues.* FROM venues
    JOIN concerts ON venues.id = concerts.venue_id
    WHERE concerts.band_id = ?
    """
    cursor = connection.execute(query, (band_id,))
    return cursor.fetchall()

def play_in_venue(band_id, venue_id, date, connection):
    query = """
    INSERT INTO concerts (band_id, venue_id, date)
    VALUES (?, ?, ?)
    """
    connection.execute(query, (band_id, venue_id, date))
    connection.commit()