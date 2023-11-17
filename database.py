import sqlite3

class GlobalDatabase:

    @staticmethod
    def get_connection():
        __connecting = sqlite3.connect('db.db')
        return __connecting

    def add_balance(self, balance, user_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET balance=balance+(?) WHERE user_id=(?)', (balance, user_id))
        conn.commit()

    def minus_balance(self, balance, user_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET balance=balance-(?) WHERE user_id=(?)', (balance, user_id))
        conn.commit()

    def add_gold(self, balance, user_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET gold=gold+(?) WHERE user_id=(?)', (balance, user_id))
        conn.commit()

    def minus_gold(self, balance, user_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET gold=gold-(?) WHERE user_id=(?)', (balance, user_id))
        conn.commit()

    def info_user(self, user_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE user_id=(?)', (user_id,))
        return c.fetchall()

    def get_all_user(self):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        return c.fetchall()

    def get_referral(self, user_id):
        conn = self.get_connection()
        c = conn.cursor()
        referral = c.execute('SELECT referral FROM users WHERE user_id=(?)', (user_id,))
        if referral:
            return c.fetchone()[0]
        else:
            return '5390216790'

    def update_gold(self, referral):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET gold=gold+5 WHERE user_id=(?)', (referral,))
        conn.commit()