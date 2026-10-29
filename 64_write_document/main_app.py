# write document dalam python
# di gunakan untuk membuat file eksternal

# buat file baru
with open("text_1.txt","w") as file:
    file.write("hello world")
# ini akan overwrite atau menimpa isinya
with open("text_1.txt","w") as file:
    file.write("hello master")

# buat file baru
with open("text_2.txt","w") as file:
    file.write("hello world\n")
# ini akan membuat baris baru di filenya
with open("text_2.txt","a") as file:
    file.write("hello master")

# buat file baru
with open("text_3.txt","w") as file:
    file.write("hello world")
# sama seperti write, ini akan menimpa isinya hanya saja per karakter
# misal master (6 char) -> world (5 char) = worldr
with open("text_3.txt","r+") as file:
    file.write("hello master")

# bedanya write dan r+ adalah write akan seolah menghapus dan memulai dari awal
# sementara r+ akan menimpa karakter per karakter



