import sqlite3

def get_band_for_concert(concert_id, connection):
    query = """
    SELECT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.id = ?
    """
    cursor = connection.execute(query, (concert_id,))
    return cursor.fetchone()

def get_venue_for_concert(concert_id, connection):
    query = """
    SELECT venues.* FROM venues
    JOIN concerts ON venues.id = concerts.venue_id
    WHERE concerts.id = ?
    """
    cursor = connection.execute(query, (concert_id,))
    return cursor.fetchone()

def is_hometown_show(concert_id, connection):
    query = """
    SELECT CASE WHEN bands.hometown = venues.city THEN 1 ELSE 0 END AS hometown_show
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    cursor = connection.execute(query, (concert_id,))
    return cursor.fetchone()[0] == 1