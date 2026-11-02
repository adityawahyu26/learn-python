from . import operasi

# Fungsi untuk menampilkan semua data buku dari database.
def read_data():
    data_file = operasi.read()
    index = "No."
    penulis = "Penulis"
    judul = "Judul Buku"
    tahun = "Tahun Terbit"

    print("="*110)
    print(f"{index:^5} | {judul:<50} | {penulis:<30} | {tahun:<10}")
    print("-"*110)

    # data_file berisi list baris dari file. Setiap baris adalah satu record.
    # Karena kita simpan sebagai CSV, maka setiap record bisa dipisah dengan split(',').
    for index, data in enumerate(data_file):
        # Hilangkan newline di akhir baris agar tidak ikut masuk ke data.
        data = data.strip()

        # Abaikan baris kosong jika ada.
        if not data:
            continue

        # Pisahkan field berdasarkan koma.
        data_break = data.split(",")

        # Jika field tidak lengkap, lewati baris tersebut.
        if len(data_break) < 5:
            continue

        # Ambil nilai masing-masing kolom.
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        # Tampilkan data dengan format rapi.
        print(f"{index+1:^5} | {judul:.50} | {penulis:.30} | {tahun:<10}")

    print("="*110,"\n")

def create_data():
    # Meminta input dari pengguna untuk data buku baru.
    print("\nMasukkan data buku baru:")
    print("-"*30)
    penulis = input("Masukkan nama penulis: ")
    judul = input("Masukkan judul buku: ")
    while True:
        try :
            tahun = int(input("Masukkan tahun terbit: "))
            if len(str(tahun)) == 4: 
                break
            else:
                print("Tahun terbit harus terdiri dari 4 digit. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan tahun terbit yang benar.")
   
    # Memanggil fungsi create dari modul operasi untuk menyimpan data baru.
    operasi.create(penulis, judul, tahun)
    print("Data berhasil ditambahkan!\n")
