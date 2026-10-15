# list angka
angka = [2,4,4,3,2,6,8,5,7,8,7,6,9,5,3,5,9,7,4,2,4,2,2,1,1,9,8,6,5]
print(f"data angka =\n{angka}")

# menghitung jumlah data tertentu di dalam list
# menghitung angka 3
angka_3 = angka.count(3)
print(f"\njumlah angka 3 adalah = {angka_3}")
# menghitung angka 4
angka_4 = angka.count(4)
print(f"jumlah angka 4 adalah = {angka_4}")

# data list string
makanan = ["martabak", "gado-gado", "seblak", "siomay"]
print(f"\ndata makanan =\n{makanan}")

# menampilkan index list string
index_martabak = makanan.index("martabak")
index_siomay = makanan.index("siomay")
print(f"\nindex data martabak = {index_martabak}")
print(f"index data siomay = {index_siomay}")

# mengurutkan data list
# dari kecil ke besar
print(f"\ndata angka sebelum diurutkan =\n{angka}")
angka.sort()
print(f"data angka setelah diurutkan =\n{angka}")
# dari alfabet a-z
print(f"\ndata makanan sebelum diurutkan =\n{makanan}")
makanan.sort()
print(f"data makanan setelah diurutkan =\n{makanan}")

# reverse data
# dari besar ke kecil
angka.reverse()
# dari alfabet z-a
makanan.reverse()
# menampilkan keduanya
print(f"\ndata setelah direverse =\n{angka}\n{makanan}")

