import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name text, description text, "
                         "price text) ")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS user (userid INTEGER PRIMARY KEY, name text, email text, "
            "phone_num text) ")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM item")
        rows = self.cur.fetchall()
        return rows

    def fetch2(self):
        self.cur.execute("SELECT * FROM user")
        rows2 = self.cur.fetchall()
        return rows2

    def insert(self, name, description, price):
        self.cur.execute("INSERT INTO item VALUES(NULL,?,?,?)", (name, description, price))
        self.conn.commit()

    def insert_user(self, name, email, phone_num):
        self.cur.execute("INSERT INTO user VALUES(NULL,?,?,?)", (name, email, phone_num))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM item WHERE id=?", (id,))
        self.conn.commit()

    def remove_user(self, userid):
        self.cur.execute("DELETE FROM user WHERE userid=?", (userid,))
        self.conn.commit()

    def update(self, id, name, description, price):
        self.cur.execute("UPDATE item SET name=?, description=?,price=? WHERE id = ?",
                         (name, description, price, id))
        self.conn.commit()

    def update_user(self, userid, name, email, phone_num):
        self.cur.execute("UPDATE user SET name=?, email=?, phone_num=? WHERE userid = ?",
                         (name, email, phone_num, userid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('thriftstore.db')
# db.insert("Shirt", "size small blue shirt", "5")
# db.insert("Pants", "size 14 straight cut jeans", "10")
# db.insert("T-shirt", "large band t", "7")
