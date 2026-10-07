# mengambil input dari user
# akan selalu bertipe data string
# kecuali jika di casting dulu

# mengambil input dengan tipe data string
nama = input("Masukkan nama Anda: ")

# mengambil input dengan tipe data integer
umur = int(input("Masukkan umur Anda: "))

# mengambil input dengan tipe data float
tinggi = float(input("Masukkan tinggi badan Anda (meter): "))

# mengambil input dengan tipe data boolean
jawaban = bool(int(input("Apakah Anda suka pemrograman? (1 = ya/ 0 = tidak): ")))

# menampilkan output
print("======")
print("Nama Anda adalah:", nama)
print("Umur Anda adalah:", umur, "tahun")
print("Tinggi badan Anda adalah:", tinggi, "meter")
print("Jawaban Anda adalah:", jawaban)


