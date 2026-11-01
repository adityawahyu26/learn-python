from . import Database
from .utility import random_number
import time

# Fungsi untuk membuat data awal ke database.
def create_first_data():
    penulis = input("penulis: ")
    judul = input("judul: ")
    tahun = input("tahun: ")

    # Copy template data yang sudah dibuat di Database.py.
    data = Database.TEMPLATE.copy()

    # Isi data utama sesuai input user.
    data["pk"] = random_number(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    # Simpan data dalam format CSV agar mudah dibaca kembali oleh split(',').
    # Catatan: kita menggunakan koma sebagai pemisah antar field.
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try:
        with open(Database.DB_NAME, "w", encoding='utf-8') as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error: {e}")

# Fungsi untuk membaca isi file database.
def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            data = file.readlines()
            return data
    except Exception as e:
        print(f"Error: {e}")
        return False
