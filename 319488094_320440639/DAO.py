from DTO import Hat, Supplier, Order


class Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, hatDTO):
        self.conn.execute("""
            INSERT INTO hats(id, topping, supplier, quantity) VALUES (?,?,?,?)
        """, [hatDTO.id, hatDTO.topping, hatDTO.supplier, hatDTO.quantity])

    def find(self, topping):
        c = self.conn.cursor()
        all = c.execute("""
        SELECT id, topping, supplier, quantity FROM hats WHERE topping = ?
        """, [topping]).fetchall()
        list = [Hat(*row) for row in all]
        if len(list)>0:
            toReturn = list[0]
            for row in list:
                if row.supplier < toReturn.supplier:
                    toReturn = row

            return toReturn

        return None

    def update(self, hat):
        self.conn.execute("""
            UPDATE hats SET quantity=(?) WHERE id=(?) 
        """, [hat.quantity - 1, hat.id])

    def remove(self, hat):
        self.conn.execute("""
            DELETE FROM hats WHERE id=(?)
        """, [hat.id])


class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, supplierDTO):
        self.conn.execute("""
            INSERT INTO suppliers(id, name) VALUES (?,?)
        """, [supplierDTO.id, supplierDTO.name])

    def find(self, id):
        c = self.conn.cursor()
        c.execute("""
            SELECT id,name FROM suppliers WHERE id = (?)
        """, [id])

        return Supplier(*c.fetchone())




class Orders:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, orderDTO):
        self.conn.execute("""
            INSERT INTO orders(id, location, hat) VALUES (?,?,?)
        """, [orderDTO.id, orderDTO.location, orderDTO.hat])
