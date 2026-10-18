# copy dan pop dalam dictionary

siswa_akademiya = {
    "cl":"collei",
    "wd":"wanderer",
    "ly":"layla"
}
print(siswa_akademiya)

# copy 
copy_siswa = siswa_akademiya.copy()
print(copy_siswa)
# jika salah satu datanya diubah, maka copynya akan sama seperti sebelumnya
siswa_akademiya["wd"] = "kunikuzi"
print(f"\nini adalah data awal =\n{siswa_akademiya}")
print(f"ini adalah data copy =\n{copy_siswa}")

# pop, mengambil data dari dictionary dan menyimpannya di variable
data_layla = siswa_akademiya.pop("ly")
print(f"\nini adalah data setelah pop =\n{siswa_akademiya}")
print(f"ini data hasil popnya = {data_layla}")

# popitem, mengambil data terakhir
data_akhir = siswa_akademiya.popitem()
print(f"\nini adalah data setelah popitem =\n{siswa_akademiya}")
print(f"ini data hasil popitemnya = {data_akhir}")




