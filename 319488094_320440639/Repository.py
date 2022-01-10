import sqlite3
import os
import imp
import atexit

from DAO import Hats, Suppliers, Orders


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.hats = Hats(self._conn)
        self.suppliers = Suppliers(self._conn)
        self.orders = Orders(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        
            CREATE TABLE suppliers (
                id INT PRIMARY KEY,
                name TEXT NOT NULL
                );
                
            CREATE TABLE hats (
            id INT PRIMARY KEY , 
            topping TEXT NOT NULL,
            supplier INT NOT NULL,
            quantity INT NOT NULL,
            
            FOREIGN KEY(supplier)  REFERENCES suppliers(id)
            );
            
            CREATE TABLE orders (
            id INT PRIMARY KEY,
            location TEXT NOT NULL,
            hat INT NOT NULL,
            
            FOREIGN KEY(hat) REFERENCES hats(id)
            );
        
        """)


repo = _Repository()

atexit.register(repo.close)

