from . import Database
from .utility import random_number
import time

def _now():
    # waktu lokal + offset zona waktu, contoh: 2026-11-03-09-15-00+0700
    return time.strftime("%Y-%m-%d-%H-%M-%S%z", time.localtime())

def create_first_data():
    penulis = input("penulis buku: ")
    judul = input("judul buku: ")
    while True:
        try:
            tahun = int(input("tahun terbit: "))
            if len(str(tahun)) == 4:   # sebelumnya len(tahun) -> TypeError, int tidak punya len
                break
            else:
                print("Tahun terbit harus terdiri dari 4 digit. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan tahun terbit yang benar.")

    data_str = Database.format_record(random_number(6), _now(), penulis, judul, tahun)

    try:
        with open(Database.DB_NAME, "w", newline="", encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error: {e}")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r", encoding="utf-8") as file:
            data = file.readlines()
            jumlah_buku = len(data)
            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku >= jumlah_buku:   # sebelumnya > (off-by-one)
                    return False
                return data[index_buku]
            return data
    except Exception as e:
        print(f"Error: {e}")
        return False

def create(penulis, judul, tahun):
    data_str = Database.format_record(random_number(6), _now(), penulis, judul, tahun)

    try:
        with open(Database.DB_NAME, "a", newline="", encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error: {e}")

def update(no_buku, pk, date_add, penulis, judul, tahun):
    data = Database.format_record(pk, date_add, penulis, judul, tahun).encode("utf-8")
    offset = Database.RECORD_LENGTH * (no_buku - 1)

    # Pengaman: kalau panjang record tidak 549 byte, lebih baik menolak daripada merusak file.
    if len(data) != Database.RECORD_LENGTH:
        print(f"Error: panjang record {len(data)} byte, seharusnya {Database.RECORD_LENGTH}")
        return

    try:
        # mode biner: tidak ada konversi newline sama sekali
        with open(Database.DB_NAME, "r+b") as file:
            file.seek(0, 2)
            if offset < 0 or offset + Database.RECORD_LENGTH > file.tell():
                print("Error: nomor buku tidak ada")
                return
            if no_buku > 1:
                file.seek(offset - 1)
                if file.read(1) != b"\n":
                    print("Error: posisi record tidak valid, file mungkin rusak")
                    return
            file.seek(offset)
            file.write(data)
    except Exception as e:
        print("Error: ", e)