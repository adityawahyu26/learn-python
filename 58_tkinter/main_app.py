# library tkinter untuk menampilkan GUI

# mengimport library tkinter dan ttk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# inisiasi menjadi objek
window = tk.Tk()

# ubah warna background, ukuran, tidak boleh di hard resize dan menambahkan title
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("hello world")

# variable
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# function
def submit():
    pesan = f"halo, selamat datang {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="welcome",message=pesan)

# membuat frame untuk input
input_frame = ttk.Frame(window)
# beberapa opsi untuk menampilkan. grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# membuat label untuk var nama depan
nama_depan_label = ttk.Label(input_frame, text="nama depan :")
nama_depan_label.pack(padx=10,fill="x",expand=True)

# membuat entry untuk var nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# membuat label untuk var nama belakang
nama_belakang_label = ttk.Label(input_frame, text="nama belakang :")
nama_belakang_label.pack(padx=10,fill="x",expand=True)

# membuat entry untuk var nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

# membuat button submit
tombol_kirim = ttk.Button(input_frame,text="Submit",command=submit)
tombol_kirim.pack(padx=10,pady=10,fill="x",expand=True)

# mainloop 
window.mainloop()




