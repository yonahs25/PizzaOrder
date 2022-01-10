class Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, hatDTO):
        self.conn.execute(""""
            INSERT INTO hats(
        """)


class Supplier:
    def __init__(self,conn):
        self.conn = conn
