# list dalam python
angka = [12, 34, 53, 21]
print(angka)

# cara bikin list 
# bikin bilangan 10 index
# dari index 0 sampai 9
# range(index awal, jumlah index, kelipatan)
angka1 = range(0,10,2) # ini cara yang kurang tepat
print(angka1) #outputnya akan hard raw
angka2 = list(angka1) # casting dulu ke type list
print(angka2) # baru outputnya akan valid

# pakai metode for loop / list comprehensif
angka3 = [i for i in range(0,10)] 
print(angka3)

# pakai if dan hanya bilangan genap
angka4 = [i for i in range(0,10) if i%2 == 0] 
print(angka4)

# pakai if dan hanya bilangan ganjil
angka5 = [i for i in range(0,10) if i%2 != 0] 
print(angka5)