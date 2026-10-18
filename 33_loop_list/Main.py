# loop dalam list

# for loop
print("for loop")
angka1 = [32,42,12,45,21]
# outputnya akan mencetak semua value listnya
for i in angka1:
    print(f"angka => {i}")

# for loop dan range
print("\nfor loop dan range")
nama1 = ["yoimiya","nilou","furina","citlali"]
length = len(nama1)
# outputnya akan berupa indexnya
for a in range(length):
    print(f"nama => {a}")

# while loop
print("\nwhile loop")
nama1 = ["yoimiya","nilou","furina","citlali"]
length = len(nama1)
a = 0
while a < length:
    print(f"nama => {nama1[a]}")
    a += 1

# list comprehension
angka1 = [32,42,12,45,21]
print("\nlist comprehension")
[(print(f"angka => {a}")) for a in angka1]

# kuadrat
print("\nangka kuadrat")
angka1 = [32,42,12,45,21]
kuadrat = [a**2 for a in angka1]
print(kuadrat)

# enumerate
print("\nenumerate")
nama1 = ["yoimiya","nilou","furina","citlali"]
for index,data in enumerate(nama1):
    print(f"index => {index}, data => {data}")




