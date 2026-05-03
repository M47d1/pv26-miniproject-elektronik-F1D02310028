import sqlite3

class DatabaseHandler:
    def __init__(self, db_name="inventaris.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS peralatan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            kategori TEXT,
            kondisi TEXT,
            tanggal TEXT,
            harga REAL
        )
        """
        with self.connect() as conn:
            conn.execute(query)

    def insert_peralatan(self, data):
        query = "INSERT INTO peralatan (nama, kategori, kondisi, tanggal, harga) VALUES (?, ?, ?, ?, ?)"
        with self.connect() as conn:
            conn.execute(query, data)

    def fetch_all(self):
        with self.connect() as conn:
            return conn.execute("SELECT * FROM peralatan").fetchall()

    def delete_peralatan(self, item_id):
        with self.connect() as conn:
            conn.execute("DELETE FROM peralatan WHERE id = ?", (item_id,))