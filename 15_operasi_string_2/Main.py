# operator dalam bentuk method untuk string

# 1. merubah case dari string
# merubah semua ke upper case
nama = "aditya wahyu"
print(nama.upper())
# merubah semua ke lower case
ab = "sASDSXsdaWDAs"
print(ab.lower())

print("\n================\n")

# 2. pengecekan dengan isX method
# cek lower atau upper case
print("untuk " + nama + "\napa lower case: " + str(nama.islower()))
print("untuk " + ab + "\napa upper case: " + str(ab.isupper()))
# isalpha() cek semuanya huruf
# isalnum() huruf dan angka
# isdecimal() angka saja
# isspace() spasi, tab, newline \n
# istitle() semua kata dimulai huruf besar
print("untuk " + nama + "\napa ini title : " + str(nama.istitle()))

print("\n================\n")

# 3. cek komponen
ad = "aditya wahyu"
print(ad)
print("apa startswith dengan 'aditya': " + str(ad.startswith('aditya')))
print("apa endswith dengan 'wahyu': " + str(ad.endswith('wahyu')))

print("\n================\n")

# 4. penggabungan komponen
# join()
buah = ["apel", "jeruk", "melon"]
join = " ".join(buah)
print(join)
# split()
print(join.split(" "))

print("\n================\n")

# 5. alokasi karakter rjust(), ljust(), center()
kanan = "right".rjust(10)
print("'" + kanan + "'")
kiri = "left".ljust(10)
print("'" + kiri + "'")
tengah = "center".center(10, "-")
print("'" + tengah + "'")
# kebalikan
tengah = tengah.strip("-")
print("'" + tengah + "'")



