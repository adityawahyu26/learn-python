# nested list
# membuat list di dalam list
a = [1,2]
b = [3,4]

# ini adalah nestednya
ab = [a,b]
print(ab)

# contoh case untuk list peserta
peserta_0 = ["kazuha", 20, "inazuma"]
peserta_1 = ["tighnari", 22, "sumeru"]
peserta_2 = ["noelle", 18, "mondstadt"]

# semua list setiap individu di nested
list_peserta = [peserta_0,peserta_1,peserta_2]

# menggunakan perulangan untuk tampilan lebih rapi bagi nestednya
for peserta in list_peserta:
    print(f"nama \t= {peserta[0]}")
    print(f"umur \t= {peserta[1]}")
    print(f"asal \t= {peserta[2]}")
    print("")

# membuat copy dari nested list
list_copy = list_peserta.copy()
print(list_copy)

# mencoba mengedit di data awal
peserta_0[0] = "yoimiya"

# dan hasilnya baik yang nested list maupun copy an ikut berubah
# hal ini terjadi karena reference nya sama
# jadi perlu pendekatan berbeda
print(list_copy)
print(list_peserta)

