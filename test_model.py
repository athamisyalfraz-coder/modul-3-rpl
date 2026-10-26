from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

# Inisialisasi Model
buku_model = BukuModel()
anggota_model = AnggotaModel()

# ==========================================
# 1. MENAMBAHKAN 3 DATA BUKU
# ==========================================
print("Menambahkan data buku...")
buku_model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
buku_model.create_buku("Basis Data Relational", "C.J. Date", 2021)
buku_model.create_buku("Sistem Informasi Manajemen", "Kenneth C. Laudon", 2022)
print("3 Data buku berhasil disimpan ke Laragon MySQL!\n")

# ==========================================
# 2. MENAMBAHKAN 3 DATA ANGGOTA
# ==========================================
print("Menambahkan data anggota...")
anggota_model.create_anggota("Ahmad Dahlan", "Jl. Trans Sulawesi No. 45, Palu")
anggota_model.create_anggota("Citra Dewi", "Jl. Soekarno Hatta No. 88, Palu")
anggota_model.create_anggota("Eko Prasetyo", "Jl. Tadulako No. 12, Palu")
print("3 Data anggota berhasil disimpan ke Laragon MySQL!\n")

# ==========================================
# 3. MENAMPILKAN DAFTAR BUKU
# ==========================================
print("=== Daftar Buku ===")
daftar_buku = buku_model.get_all_buku()
for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})"
    )

# ==========================================
# 4. MENAMPILKAN DAFTAR ANGGOTA
# ==========================================
print("\n=== Daftar Anggota ===")
daftar_anggota = anggota_model.get_all_anggota()
for anggota in daftar_anggota:
    print(
        f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}"
    )