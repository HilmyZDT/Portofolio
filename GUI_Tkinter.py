import sqlite3
import tkinter as tk
from tkinter import ttk #Themed Tkinter
import tkinter.messagebox

class Mahasiswa:
    db_name = "data.db"

    def __init__(self, root):
        self.root = root
        self.root.title("Program CRUD Mahasiswa")

        # membuat frame untuk input data mahasiswa
        self.input_frame = ttk.LabelFrame(text=" Input Data Mahasiswa ")
        self.input_frame.pack(side=tk.LEFT, padx=20)

        # membuat widget untuk input NIM
        self.nim_label = ttk.Label(self.input_frame, text="NIM :")
        self.nim_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.nim_entry = ttk.Entry(self.input_frame)
        self.nim_entry.grid(row=0, column=1, padx=5, pady=5)

        # membuat widget untuk input Nama
        self.nama_label = ttk.Label(self.input_frame, text="Nama :")
        self.nama_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.nama_entry = ttk.Entry(self.input_frame)
        self.nama_entry.grid(row=1, column=1, padx=5, pady=5)

        # membuat widget untuk input Alamat
        self.alamat_label = ttk.Label(self.input_frame, text="Alamat :")
        self.alamat_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.alamat_entry = ttk.Entry(self.input_frame)
        self.alamat_entry.grid(row=2, column=1, padx=5, pady=5)

        # membuat widget untuk input Jurusan
        self.jurusan_label = ttk.Label(self.input_frame, text="Jurusan :")
        self.jurusan_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.jurusan_entry = ttk.Entry(self.input_frame)
        self.jurusan_entry.grid(row=3, column=1, padx=5, pady=5)

        # membuat frame untuk tombol aksi
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side=tk.LEFT, padx=20)

        # membuat tombol untuk menambahkan data
        self.add_button = ttk.Button(
            self.button_frame, text="Add", command=self.add_data
        )
        self.add_button.pack(fill=tk.X, padx=5, pady=5)

        # membuat tombol untuk mengedit data
        self.edit_button = ttk.Button(
            self.button_frame, text="Edit", command=self.edit_data
        )
        self.edit_button.pack(fill=tk.X, padx=5, pady=5)

        # Tombol Delete data
        self.delete_button = ttk.Button(
            self.button_frame, text="Delete", command=self.delete_data
        )
        self.delete_button.pack(fill=tk.X, padx=5, pady=5)

        # Tabel Data
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        self.tree = ttk.Treeview(
            self.table_frame,
            columns=("NIM", "Nama", "Alamat", "Jurusan"),
            show="headings",
            height=10,
        )

        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Alamat", text="Alamat")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Panggil fungsi untuk menampilkan data pada tabel
        self.create_table()
        self.show_data()

        def on_close():
            response = tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
            if response:
                self.root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', on_close)

    def run(self):
        self.root.mainloop()

    def execute_query(self, query, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def create_table(self):
        # Kolom Tabel
        query = """CREATE TABLE IF NOT EXISTS Mahasiswa (
            NIM INTEGER PRIMARY KEY,
            Nama TEXT,
            Alamat TEXT,
            Jurusan TEXT
            )"""
        # params = (nim, nama, alamat, jurusan)
        self.execute_query(query=query)

    def show_data(self):
        # Kosongkan tabel
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)

        # Ambil data dari database dan tampilkan pada tabel
        query = "SELECT NIM, Nama, Alamat, Jurusan FROM Mahasiswa"
        data = self.execute_query(query).fetchall()
        for row in data:
            self.tree.insert("", tk.END, values=row)

    def add_data(self):
        # Ambil data dari input user
        nim = self.nim_entry.get()
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get() 
        jurusan = self.jurusan_entry.get()

        # Validasi input
        if not nim.isdigit():
            tkinter.messagebox.showerror("Error", "NIM harus berupa angka")
            return

        # Cek apakah ada input yang kosong
        if nim == "" or nama == "" or alamat == "" or jurusan == "":
            tkinter.messagebox.showerror("Error", "Mohon lengkapi semua input")
            return

        # Cek apakah NIM sudah ada di database
        query = "SELECT COUNT(*) FROM Mahasiswa WHERE NIM = ?"
        params = (nim,)
        result = self.execute_query(query, params).fetchone()

        if result[0] > 0:
            tkinter.messagebox.showerror("Error", "NIM sudah terdaftar dalam database")
            return

        # Insert data ke dalam database
        query = "INSERT INTO Mahasiswa (NIM, Nama, Alamat, Jurusan) VALUES (?, ?, ?, ?)"
        params = (nim, nama, alamat, jurusan)
        self.execute_query(query, params)

        # Bersihkan input setelah data ditambahkan ke dalam database
        self.clear_entries()

        # Tampilkan data terbaru pada tabel
        self.show_data()

    def edit_data(self):
        if not self.tree.focus():
            tkinter.messagebox.showwarning(
                title="Warning", message="Please select data to edit"
            )
            return
        
        # Ambil data dari input user
        nim = self.nim_entry.get()
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        jurusan = self.jurusan_entry.get()

        # Ambil ID data yang akan di-update
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        id = values[0]

        # Validasi input
        if not nim.isdigit():
            tkinter.messagebox.showerror("Error", "NIM harus berupa angka")
            return

        # Cek apakah ada input yang kosong
        if nim == "" or nama == "" or alamat == "" or jurusan == "":
            tkinter.messagebox.showerror("Error", "Mohon lengkapi semua input")
            return
        
        # Cek apakah NIM sudah ada di database, kecuali jika NIM tersebut adalah NIM dari data yang akan di-update
        query = "SELECT COUNT(*) FROM Mahasiswa WHERE NIM = ? AND NIM <> ?"
        params = (nim, id)
        result = self.execute_query(query, params).fetchone()

        if result[0] > 0:
            tkinter.messagebox.showerror("Error", "NIM sudah terdaftar dalam database")
            return

        # Update data pada database
        query = "UPDATE Mahasiswa SET NIM=?, Nama=?, Alamat=?, Jurusan=? WHERE NIM=?"
        params = (nim, nama, alamat, jurusan, id)
        self.execute_query(query, params)

        # Clear input fields
        self.clear_entries()

        # Tampilkan data terbaru pada tabel
        self.show_data()

    def clear_entries(self):
        self.nim_entry.delete(0, tk.END)
        self.nama_entry.delete(0, tk.END)
        self.alamat_entry.delete(0, tk.END)
        self.jurusan_entry.delete(0, tk.END)
        self.show_data()

    def delete_data(self):
        if not self.tree.focus():
            tkinter.messagebox.showwarning(
                title="Warning", message="Please select data to delete"
            )
            return

        result = tkinter.messagebox.askquestion(
            title="Delete Confirmation", message="Are you sure to delete this data?"
        )
        if result == "yes":
            selected_item = self.tree.focus() 
            nim = self.tree.item(selected_item)["values"][0]
            query = f"DELETE FROM Mahasiswa WHERE nim = {nim}"
            self.execute_query(query=query)

            # Tampilkan data terbaru pada tabel
            self.show_data()

    
if __name__ == "__main__": 
    app = Mahasiswa(root=tk.Tk()) 
    app.root.mainloop() 