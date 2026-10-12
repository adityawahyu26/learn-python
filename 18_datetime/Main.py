# import library datetime
import datetime as dt

# # inisiasi 
# today = dt.date.today()
# print(today)

# # tanggal lahir
# birthday = dt.date(2005,2,26)
# print(birthday)
# hari_lahir = f"hari {birthday:%A}"
# print(hari_lahir)

print("Masukkan Tanggal Lahir Anda: \n")

date = int(input("Tanggal \t: "))
month = int(input("Bulan \t\t: "))
year = int(input("Tahun \t\t: "))

birthday = dt.date(year,month,date)
tanggal_lahir = f"tanggal lahir anda : {birthday}"
print(tanggal_lahir)
hari_lahir = f"hari lahir anda : {birthday:%A}"
print(hari_lahir)
today = dt.date.today()
umur_hari = today - birthday
umur_tahun = umur_hari.days // 365
sisa_bulan = (umur_hari.days % 365) // 30
sisa_hari = (umur_hari.days % 365) % 30
print(f"Umur Anda : {umur_tahun} tahun, {sisa_bulan} bulan, {sisa_hari} hari")



