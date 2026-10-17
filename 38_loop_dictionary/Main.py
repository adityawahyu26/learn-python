# looping dalam dictionary

data_dict = {
    "mie":"mie ayam",
    "nasi":"nasi goreng",
    "es":"es teh"
}

# for loop untuk dict, hasilnya akan menampilkan key nya
print("ini adalah for loop")
for a in data_dict:
    print(a)

# outputnya hanya menampilkan key / identifiernya
print("\nini menggunakan keys")
for a in data_dict.keys():
    print(a)

# outputnya menampilkan value / nilainya
print("\nini menggunakan values")
for b in data_dict.values():
    print(b)

# outputnya menampilkan key dan value
print("\nini menggunakan items")
for c in data_dict.items():
    print(c)

# menampilkan key dan value dengan lebih rapi
print("\nmenampilkan key, value di items")
for key,value in data_dict.items():
    print(f"key {key}, value = {value}")



