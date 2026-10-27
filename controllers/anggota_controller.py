import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View Anggota
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding tombol simpan di View Anggota
        self.view.btn_simpan.configure(command=self.simpan_data)

        # Memuat data ke tabel anggota saat pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke dalam tabel View (sesuai kolom id, nama, alamat)
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def simpan_data(self):
        # Mengambil teks dari form di View
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        # Validasi Form Kosong
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            # Membersihkan form input
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_alamat.delete(0, 'end')
            # Memuat ulang tabel agar data terbaru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def run(self):
        self.view.mainloop()