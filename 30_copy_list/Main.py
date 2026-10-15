# copy list

## metode ini akan copy sama persis
# tapi jika salah satu diubah 
# maka yang lain juga ikut berubah
a = [23,45,32,45,32]
b = a
print(f"nilai a = {a}")
print(f"nilai b = {b}")
# idnya juga sama persis
print(f"id list a = {hex(id(a))}")
print(f"id list b = {hex(id(b))}")
# misal jika di a diubah maka b berubah juga, begitu juga sebaliknya
a[0] = 100
print("mengubah salah satu nilai, a")
print(f"nilai a = {a}")
print(f"nilai b = {b}")

## metode copy yang benar
c = a.copy()
print("\nmetode copy yang benar")
print(f"nilai a = {a}")
print(f"nilai b = {b}")
print(f"nilai c = {c}")
# id a dan b akan sama karena metodenya kurang tepat
# tapi c akan berbeda dari keduanya
print(f"id list a = {hex(id(a))}")
print(f"id list b = {hex(id(b))}")
print(f"id list c = {hex(id(c))}")
# jika edit isi c maka a dan b tidak akan berubah isinya
c[1] = 26
print("mengubah salah satu nilai, c")
print(f"nilai a = {a}")
print(f"nilai b = {b}")
print(f"nilai c = {c}")

# metode yang benar adalah c
# penerapan b kurang tepat karena jika salah satu diubah, semuanya berubah
# di c jika c berubah, maka yang lain tidak akan berubah
# b memiliki id yang sama persis dengan a
# sedangkan c memiliki id yang berbeda dari a maupun b
