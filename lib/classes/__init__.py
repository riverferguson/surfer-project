import sqlite3

CONN = sqlite3.connect('lib/db/database.db')
CURSOR = CONN.cursor()
