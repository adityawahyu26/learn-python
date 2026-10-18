# latihan dictionary 1
import datetime as dt
import os

# membuat template dict nya
player_template = {
    "nama":"nama",
    "posisi":"posisi",
    "negara":"negara",
    "usia":20,
    "tanggal_lahir":dt.datetime(1111,1,11)
}

# membuat wadah dict kosong
data_player = {}

# os dipakai untuk ui yang lebih rapi
os.system("cls")
print("FOOTBALLERS DATA")
print("-"*20)

# dict.fromkey untuk mengambil referensi key dari template
player = dict.fromkeys(player_template)
player["nama"] = input("nama : ")
player["posisi"] = input("posisi : ")
player["negara"] = input("negara : ")
player["usia"] = int(input("usia : "))
TAHUN = int(input("tahun lahir(YYYY) : "))
BULAN = int(input("bulan lahir (1-12) : "))
TANGGAL = int(input("tanggal lahir(1-31) : "))
player["tanggal_lahir"] = dt.datetime(TAHUN,BULAN,TANGGAL)

print(f"\n{player}")