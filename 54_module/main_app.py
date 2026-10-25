# module dalam python
# module dipakai sebagai alat untuk bisa dipanggil dan digunakan untuk tugas tertentu

# case 1, import biasa
import funct 
# case 2, import dengan alias atau as
import funct_1 as f
# case 3, import dengan inisiasi fitur yang dibutuhkan
from funct_2 import tambah, kali, pangkat
# case 4, import dengan inisiasi fitur dan memberikan alias secara bersamaan
from funct_3 import tambah as add
from funct_3 import kali as k
from funct_3 import pangkat as p

# menggunakan case 1
hasil = funct.tambah(2,3,4)
print(hasil)

# menggunakan case 2
hasil_f = f.kali(3,6,4)
print(hasil_f)

# menggunakan case 3
hasil_pangkat = pangkat(3)
print(f"hasil pangkatnya adalah = {hasil_pangkat(3)}")

# menggunakan case 4
hasil_add = add(23,12,34)
print(hasil_add)

hasil_k = k(2,3,4)
print(hasil_k)

hasil_p = p(2)
print(f"hasil dari pangkatnya adalah = {hasil_p(7)}")