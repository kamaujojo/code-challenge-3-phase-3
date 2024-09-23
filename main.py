import sqlite3
from db_setup import create_tables
from band import get_concerts_for_band, play_in_venue
from venue import get_concerts_for_venue
from concert import is_hometown_show

connection = sqlite3.connect('concerts.db')

# Create the tables (you only need to run this once)
create_tables(connection)

def main():
    band_id = 1
    concerts = get_concerts_for_band(band_id, connection)
    print(concerts)
    
    play_in_venue(band_id, 1, '2024-09-22', connection)
    is_hometown = is_hometown_show(1, connection)
    print(f"Is it a hometown show? {is_hometown}")

if __name__ == "__main__":
    main()