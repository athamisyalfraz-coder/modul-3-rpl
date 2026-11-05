
import hashlib
from config.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register_user(self, username, password, role):
        if self.conn:
            cursor = self.conn.cursor()
            password_hash = self.hash_password(password)

            query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
            values = (username, password_hash, role)

            try:
                cursor.execute(query, values)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print("Gagal register:", e)
                cursor.close()
                return False

        return False

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)

            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user

        return None
