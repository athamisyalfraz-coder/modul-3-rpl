from unittest.mock import MagicMock
from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

def test_create_and_get_buku():
    # Inisialisasi model buku dengan mock koneksi database
    buku_model = BukuModel()
    buku_model.conn = MagicMock()
    mock_cursor = MagicMock()
    buku_model.conn.cursor.return_value = mock_cursor

    # Uji fungsi create_buku
    buku_model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
    mock_cursor.execute.assert_called()

    # Uji fungsi get_all_buku
    mock_cursor.fetchall.return_value = [
        {"id_buku": 1, "judul": "Pemrograman Python MVC", "penulis": "Guido van Rossum", "tahun_terbit": 2023}
    ]
    daftar_buku = buku_model.get_all_buku()
    assert isinstance(daftar_buku, list)

def test_create_and_get_anggota():
    # Inisialisasi model anggota dengan mock koneksi database
    anggota_model = AnggotaModel()
    anggota_model.conn = MagicMock()
    mock_cursor = MagicMock()
    anggota_model.conn.cursor.return_value = mock_cursor

    # Uji fungsi create_anggota
    anggota_model.create_anggota("Ahmad Dahlan", "Jl. Trans Sulawesi No. 45, Palu")
    mock_cursor.execute.assert_called()

    # Uji fungsi get_all_anggota
    mock_cursor.fetchall.return_value = [
        {"id_anggota": 1, "nama": "Ahmad Dahlan", "alamat": "Jl. Trans Sulawesi No. 45, Palu"}
    ]
    daftar_anggota = anggota_model.get_all_anggota()
    assert isinstance(daftar_anggota, list)