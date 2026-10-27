# open dan with dalam python
# untuk mengakses file external

# mengakses file eksternal dengan mode read
file = open("document.txt",mode="r")
# mengakses file eksternal dengan mode write
# file = open("document.txt",mode="w")

print("metode read file external dengan open")
# cek apq file bisa dibaca
print("apa file ini readable =", file.readable())
# cek apq file bisa ditulis
print("apa file ini writeable =", file.writable())

# mencetak semua baris dalam file
# print(file.read())
# mencetak satu baris
print(file.readline(),end="")
print(file.readline(),end="")

# cek apa file yang diakses sudah di close
print("\napa file ini sudah closed =", file.closed)
# close file yang sudah diakses
file.close()
# lalu cek lagi apa file yang diakses sudah diclose
print("apa file ini sudah closed =", file.closed)

print("\nmetode read file external dengan with")

# menggunakan mode read untuk akses file external
with open("document.txt",mode="r") as file:
    # mengambil satu baris dari file
    content = file.readline()
    # kemudian mencetaknya
    print(content)
# cek apa file yang diakses sudah diclose
print("apa file ini sudah closed =", file.closed)




