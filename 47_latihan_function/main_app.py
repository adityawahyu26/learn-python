# latihan function 
# program menghitung luas dan keliling persegi panjang

import os

# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# PANJANG = int(input("Masukkan nilai panjang: "))
# LEBAR = int(input("Masukkan nilai lebar: "))

# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

# fungsi header
def header():
     os.system("cls")
     print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
     print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
     print(f"{'-'*40:^40}")

# fungsi mengambil input user
def input_user():
     panjang = int(input("Masukkan nilai panjang: "))
     lebar = int(input("Masukkan nilai lebar: "))
     return panjang, lebar

# fungsi menghitung luas
def hitung_luas(panjang,lebar):
     return panjang*lebar

# fungsi menghitung keliling
def hitung_keliling(panjang,lebar):
     keliling = 2*(panjang+lebar)
     return keliling

# fungsi menampilkan hasil
def tampilkan_hasil(display,luas,keliling):
     display_clean = display.strip().lower()
     if display_clean in ["keduanya","dua-duanya","dua duanya"]:
          print(f"hasil perhitungan luas = {luas}")
          print(f"hasil perhitungan keliling = {keliling}")
     elif display_clean == "luas":
          print(f"hasil perhitungan luas = {luas}")
     elif display_clean == "keliling":
          print(f"hasil perhitungan keliling = {keliling}")
     else:
          print("masukkan input yang valid!")

# program utamanya
while True:
     header()
     PANJANG, LEBAR = input_user()
     LUAS = hitung_luas(PANJANG,LEBAR)
     KELILING = hitung_keliling(PANJANG,LEBAR)

     print("\napa hasil perhitungan yang ingin anda lihat?")
     howdisplay = input("luas, keliling, atau keduanya: ")
     display = tampilkan_hasil(howdisplay,LUAS,KELILING)   
     
     isdone = input("\napa anda ingin lanjut melakukan perhitungan (y/n): ")
     if isdone == "n":
          break




