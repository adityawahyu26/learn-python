# pass dan continue dalam loop python

# pass adalah dummy, kode ini tidak akan dieksekusi
batery = 0
print(f"batery saat ini {batery}%")
while batery < 100:
    batery += 10
    print(f"batery saat ini {batery}%")
    if batery == 20:
        pass
print("batery anda sudah penuh")

print("="*10)

# continue akan memotong dibawahnya dan langsung ke perulangan selanjutnya
kelas = 6

while kelas < 9:
    kelas += 1
    print(f"kamu kelas {kelas} sekarang")
    print("smt 1: uts dan semester gasal")

    if kelas == 8:
        print("smt 2 akan study tour")
        continue

    print("smt 2: uts dan semester akhir")
print("semoga lulus ya")

