
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Binding tombol
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)

        # Otorisasi khusus admin
        if self.user_role != "admin":
            self.view.btn_simpan.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku['id_buku'],
                    buku['judul'],
                    buku['penulis'],
                    buku['tahun_terbit']
                )
            )

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def update_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin!")
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data buku terlebih dahulu!")
            return

        values = self.view.tabel.item(selected[0], "values")

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return

        if self.model.update_buku(values[0], judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin!")
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data buku terlebih dahulu!")
            return

        values = self.view.tabel.item(selected[0], "values")

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?"
        )

        if konfirmasi:
            if self.model.delete_buku(values[0]):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def kosongkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def logout(self):
        self.view.destroy()

        from controllers.auth_controller import AuthController

        app_login = AuthController()
        app_login.run()

    def run(self):
        self.view.mainloop()
