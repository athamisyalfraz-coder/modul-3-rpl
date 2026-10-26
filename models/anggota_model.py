from config.database import Database


class AnggotaModel:

  def __init__(self):
    db = Database()
    self.conn = db.get_connection()

  def create_anggota(self, nama, alamat):
    cursor = self.conn.cursor()
    query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
    cursor.execute(query, (nama, alamat))
    self.conn.commit()
    cursor.close()

  def get_all_anggota(self):
    cursor = self.conn.cursor(dictionary=True)
    query = "SELECT * FROM anggota"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result