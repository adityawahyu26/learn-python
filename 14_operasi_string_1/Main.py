# operasi dan manipulasi string 1

# 1. menyambung string (concatenate)
nama_depan = "aditya"
nama_tengah = "wahyu"

nama_lengkap = nama_depan + " " + nama_tengah
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang karakternya adalah: " + str(panjang))

# 3. operator untuk string
# a. mengecek apa ada komponen char atau string di string
A = "a"
search = A in nama_lengkap
print("apa " + A + " ada didalam " + nama_lengkap + ": " + str(search))
# b. mengulang string
print("ha"*10)
# c. indexing
print("index ke-0: " + nama_lengkap[0])
print("index ke-1: " + nama_lengkap[1])
print("index ke-(-1): " + nama_lengkap[-1])
print("index ke-(-2): " + nama_lengkap[-2])
print("index ke-[0:6]: " + nama_lengkap[0:7]) # selalu tambahkan satu 
print("index genap: " + nama_lengkap[0:12:2]) # [awal, akhir, increment]
# d. item paling kecil dan item paling besar
print("item paling kecil adalah: " + min(nama_lengkap)) 
# yang terkecil adalah " " karena kode ASCII nya yang paling kecil
print("item paling besar adalah: " + max(nama_lengkap))
# yang terbesar adalah huruf y karena kode ASCII nya yang paling besar

# 4. operator dalam bentuk method
A = "a"
print(A + " muncul sebanyak: " + str(nama_lengkap.count(A)) + " kali")
# count() digunakan untuk mencari berapa banyak objek muncul dalam string


