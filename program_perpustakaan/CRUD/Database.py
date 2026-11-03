from . import operasi

# Database.py
DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd-hh-mm-ss+zzzz",   # 24 karakter, sama dengan format aslimu
    "penulis": 255 * " ",
    "judul": 255 * " ",
    "tahun": "yyyy",
}
RECORD_LENGTH = sum(len(v) for v in TEMPLATE.values()) + len(TEMPLATE)  # 549, termasuk "\n"

def format_record(pk, date_add, penulis, judul, tahun):
    return (
        f"{pk},{date_add},"
        f"{penulis[:255].ljust(255)},{judul[:255].ljust(255)},"
        f"{tahun}\n"
    )

def innit_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database siap digunakan")
    except:
        print("data belum dibuat dalam database")
        operasi.create_first_data()
