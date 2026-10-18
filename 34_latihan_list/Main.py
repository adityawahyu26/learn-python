# program list buku

# buat list kosong sebagai wadah
catalog = []

# pakai perulangan untuk terus mengulang program
while True:
    print("\nPROGRAM LIST BUKU")
    # ambil data dari input user
    judul = input("apa nama buku: ")
    penulis = input("siapa penulisnya: ")
    
    # masukkan input user ke nested list
    books = [judul,penulis]
    # masukkan nested agar selalu ditambahkan ke wadah listnya
    catalog.append(books)
    print("\n","="*18)

    # tampilkan datanya dalam list
    for index,book in enumerate(catalog):
        print(f"{index+1} | {book[0]} | {book[1]}")

    # ambil input konfirmasi user apa programnya terus berjalan / tidak
    confirm = input("\napa lanjut ingin menambah catalog buku? [y/n] : ")

    # jika user memilih n maka perulangan program berhenti
    # jika user memilih y maka perulangan program akan terus berlanjut
    if confirm == "n":
        break