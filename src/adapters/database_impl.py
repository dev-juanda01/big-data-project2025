import sqlite3
import json
from typing import List
from src.core.entities.data_record import DataRecord
from src.ports.database import Database

class DatabaseImpl(Database):
    def __init__(self):
        self.conn = sqlite3.connect('src/static/db/ingestion.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT,
                price REAL,
                description TEXT,
                category TEXT,
                images TEXT
            )
        ''')
        self.conn.commit()

    def save_data(self, data: List[DataRecord]):
        cursor = self.conn.cursor()
        for record in data:
            cursor.execute(
                'INSERT INTO products (id, title, price, description, category, images) VALUES (?, ?, ?, ?, ?, ?)',
                (
                    record.id,
                    record.title,
                    record.price,
                    record.description,
                    json.dumps(record.category),
                    json.dumps(record.images),
                ),
            )
        self.conn.commit()

    def get_data(self) -> List[DataRecord]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, price, description, category, images FROM products')
        rows = cursor.fetchall()
        return [
            DataRecord(
                row[0],
                row[1],
                row[2],
                row[3],
                json.loads(row[4]),
                json.loads(row[5]),
            )
            for row in rows
        ]