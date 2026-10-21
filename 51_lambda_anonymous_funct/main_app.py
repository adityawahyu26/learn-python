# lambda function
# dipakai untuk meringkas dan mempermudah penulisan kode

# inisiasi var dengan lambda
# var = lambda argument:eksekusi
kuadrat = lambda n:n**2
print(kuadrat(5))

# coba menggunakan list untuk lambda
list_peserta = ["venti","zhongli","raiden","nahida","furina","mavuika"]
# melakukan sort dengan panjang huruf terkecil sampai terbesar
list_peserta.sort(key=lambda x:len(x))
print(list_peserta)

# melakukan lambda dengan kumpulan list angka
list_angka = [1,2,3,4,5,6,7,8,9,10]
# angka yang kurang dari 5
angka_filter = list(filter(lambda x : x<5, list_angka))
print(angka_filter)
# angka genap
angka_genap = list(filter(lambda x : x%2 == 0, list_angka))
print(angka_genap)
# angka ganjil
angka_ganjil = list(filter(lambda x : x%2 != 0, list_angka))
print(angka_ganjil)
# angka yang merupakan kelipatan dari 3
angka_kelipatan3 = list(filter(lambda x : x%3 == 0, list_angka))
print(angka_kelipatan3)

# anonymous function
# inisiasi funct nya
def pangkat(n):
    # funct akan mengembalikan funct lambda
    return lambda x:x**n
# inisiasi var dan menyimpan pangkatnya
angka_pangkat = pangkat(2)
# n = 2
# print dan panggil varnya serta value yang ingin di print
# misal print(var(3)), jadi lambda funct x**n == 3**2
print(f"angka pangkatnya adalah: {angka_pangkat(5)}")
print(f"angka pangkatnya adalah: {angka_pangkat(7)}")
# atau bisa langsung print funct, funct(n)(x)
print(f"angka pangkatnya adalah: {pangkat(2)(6)}")








