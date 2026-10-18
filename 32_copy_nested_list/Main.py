# copy nested list

# buat dulu kumpulan datanya
country_0 = [36,12,17]
country_1 = [26,49,14]
country_2 = [15,47,52]

# lalu buat jadi nested list
country_list = [country_0,country_1,country_2]
print(country_list)

# copy dulu
print("copy =")
country_copy = country_list.copy()

# cek id nested list dan copy an
# jadi jika salah satu berubah maka yang lainnya juga berubah
print(f"id dari nested \t= {hex(id(country_list))}")
print(f"id dari copy \t= {hex(id(country_copy))}")

## solusinya menggunakan metode deepcopy
from copy import deepcopy
# lalu masukkan nested ke dalamnya
country_deepcopy = deepcopy(country_list)

# bandingkan id deepcopy dengan nested dan copy
print(f"id deepcopy \t= {hex(id(country_deepcopy))}")

# mencoba mengubah data
country_list[1][0] = 12

# melihat apa perubahan di eksekusi di tiga tempat
# di nested, copy dan deepcopy
print(f"\nnested list =\n{country_list}")
print(f"\ncopy list =\n{country_copy}")
print(f"\ndeepcopy list =\n{country_deepcopy}")

# berdasarkan uji coba barusan terlihat sebuah hasil
# list di deepcopy tidak langsung berubah hanya dengan di edit data asalnya
# rupanya deepcopy mempertahankan log terdahulu dari nested
# jadi walaupun nested dan copy berubah begitu di edit tapi deepcopy tidak

## sedikit tambahan
# ab = [[1,2],[3,4]]
# ab[0][1] = 2
# ab[1][0] = 3




