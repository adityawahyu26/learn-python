# latihan dictionary 2
import datetime as dt
import os
import random
import string

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

while True:
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

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_player.update({KEY:player})

    print(f"\n{'KEY':<7} {'NAMA':^17} {'POSISI':<10} {'NEGARA':<10} {'USIA':<5} {'TANGGAL LAHIR':<10}")
    print("-"*60)

    for pr in data_player:
        KEY = pr

        NAMA = data_player[KEY]['nama']
        POSISI = data_player[KEY]['posisi']
        NEGARA = data_player[KEY]['negara']
        USIA = data_player[KEY]['usia']
        LAHIR = data_player[KEY]['tanggal_lahir'].strftime("%x")

        print(f"{KEY:<7} {NAMA:^17} {POSISI:<10} {NEGARA:<10} {USIA:^5} {LAHIR:^10}")

    is_done = input("\napa anda ingin lanjut input data (y/n) : ")
    if is_done == "n":
        break









