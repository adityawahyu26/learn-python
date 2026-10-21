# global scope dan local scope dalam variable

# global scope, var yang bisa dipanggil dan dipakai dimana saja di dalam code
# var nama = "str" adalah global scope var
nama = "aditya"
def funct():
    print(f"my name is {nama}")
funct()

# local scope, hanya var yang bisa dipakai di dalam funct saja
# tidak bisa dipanggil / dipakai diluar funct
# var club = "str" adalah local scope var, hanya bisa dipakai dalam funct
def local():
    club = "liverpool"
    print(f"my favorite club is {club}")

local()

# mengubah value var global makanan dan harga dengan funct
makanan = "mie ayam"
harga = "10000"

# memakai funct ubah var
def ubah_menu(makanan_baru,harga_baru):
    # inisiasi var globalnya
    global makanan 
    global harga
    # assigment var global dengan var local
    makanan = makanan_baru
    harga = harga_baru

# outputnya akan berubah jika diubah menggunakan funct ubah var
print(f"sebelum diubah = {makanan},{harga}")
ubah_menu("nasi goreng",12000)
print(f"setelah diubah = {makanan},{harga}")

# di for / loop var local scope masih bisa dipanggil dan pakai diluar funct
count = 0
for x in range(0,5):
    count += 1
print(f"ini adalah variable local scope di for loop : {count}")

# di if / percabangan var local scope masih bisa dipanggil dan pakai diluar funct
count = 0
if count < 5:
    count += 1
    sayHi = "ini adalah variable local scope di if"
print(sayHi)




