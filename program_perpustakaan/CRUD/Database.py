from . import operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "penulis":255*" ",
    "judul":255*" ",
    "tahun":"yyyy"

}

def innit_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database siap digunakan")
    except:
        print("data belum dibuat dalam database")
        operasi.create_first_data()
