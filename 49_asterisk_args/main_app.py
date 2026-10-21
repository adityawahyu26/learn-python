# asterisk args / *args pada function
# sebagai placeholder dari argument function
# sangat dinamis karena bisa menyesuaikan

# format function biasa
def nama_siswa(nama,tinggi,berat):
    print(f"dia adalah {nama}, tingginya adalah {tinggi}cm, dan berat badannya {berat}kg")

x = nama_siswa("aditya",175,82)

# *args digunakan sebagai placeholder argument function ini
# *args disini sangat dinamis menyesuaikan kebutuhan
def list_peserta(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"dia adalah {nama}, tingginya adalah {tinggi}cm, dan berat badannya {berat}kg")

y = list_peserta("anastasya",170,60)

# penerapan *args pada funct loop operasi aritmatika +
# input berapa pun yang dimasukkan user akan dieksekusi
def operasi_tambah(*args):
    count = 0
    for arg in args:
        count += arg
    return count

z = operasi_tambah(1,2,3,4)
a = operasi_tambah(20,10,30)
print(z)
print(a)


