# default argument dalam function
# function(argument=default)
# default argument muncul ketika argument tidak diisi

# otomatis langsung menampilkan defaultnya jika argument / parameter kosong
def hallo(nama="admin"):
    print(f"hallo, selamat datang {nama}!")

hallo("aditya")
hallo()

# argument 1 / parameter pertama adalah input biasa yang harus diisi
# argument 2 / parameter kedua adalah input dengan nilai defaultnya yang tidak wajib diisi
def sayHi(nama,sapaan="selamat pagi"):
    print(f"{sapaan}, {nama}!")

sayHi("aditya","selamat malam")
sayHi("aditya")

# argument / parameter bisa diubah nilainya / tetap default saat funct dipanggil
# tidak harus berurutan argumentnya untuk mengubah valuenya
def kuadrat(angka=5,kuadrat=2):
    hasil = angka**kuadrat
    return hasil

print(kuadrat())
print(kuadrat(kuadrat=3,angka=2))

# untuk argument banyak, juga bisa diubah value argumentnya saat funct dipanggil
# tidak harus berurutan, yang penting mencantumkan dengan jelas sesuai kebutuhan
def angka(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(angka())
print(angka(input1=2,input3=4))


