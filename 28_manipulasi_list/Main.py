## contoh list
makanan = ["mie ayam", "nasi goreng", "bakso"]
print(makanan)

## menampilkan data secara terpisah
makanan_0 = makanan[0]
print(f"ini adalah data ke-0 = {makanan_0}")
# menampilkan data terakhir
# gunakan index -1, untuk kedua terakhir pakai -2, dst
makanan_last = makanan[-1]
print(f"ini adalah data terakhir = {makanan_last}")

## menambahkan data baru ke list
# menyelipkan ke tengah
print(f"data sebelum ditambahkan =\n{makanan}")
makanan.insert(1, "tahu kupat") # insert(ditaruh index mana, "valuenya")
print(f"data setelah ditambahkan =\n{makanan}")
# menambahkan data di akhir
makanan.append("pecel")
print(f"data akhir setelah ditambahkan =\n{makanan}")

## menggabungkan dengan list lain
food = ["ayam geprek", "nasi padang", "soto"]
makanan.extend(food)
print(f"data setelah digabungkan =\n{makanan}")

## menghapus data dari dalam list
makanan.remove("tahu kupat")
print(f"data dihapus =\n{makanan}")
# menghapus data terakhir
makanan.pop()
print(f"data akhir dihapus =\n{makanan}")
