# function dengan return

# membuat function kuadrat
def operasiKuadrat(x):
    # melakukan operasi aritmatika kuadrat ** pada var
    kuadrat = x**2
    # menyuruh func balikin nilainya
    return kuadrat
# pakai var untuk jalanin sama nerima return func
y = operasiKuadrat(7)
# menampilkan output nilainya yang ada di var
print(y)

# bikin func aritmatika kali *
def operasiKali(x,y):
    # disini langsung eksekusi func sekaligus return
    return x * y
# tidak pakai var, bisa langsung di print
print(operasiKali(6,23))

# bikin func aritmatika +,-,*,/
def operasiMath(x,y):
    # eksekusi func dan simpan ke var
    tambah = x + y
    kurang = x - y
    kali = x * y
    bagi = x / y
    # kembalikan semua nilai dari semua var
    return tambah, kurang, kali, bagi
# simpan ke dalam beberapa var untuk funct nya
t,k,a,b = operasiMath(26,12)
# print semua varnya
print(f"hasil tambah = {t}")
print(f"hasil kurang = {k}")
print(f"hasil kali = {a}")
print(f"hasil bagi = {b}")




