# latihan membuat segitiga dengan loop
sisi = 10

# metode for loop
print("metode for loop")
count = 1
for i in range(sisi):
    print("+"*count)
    count += 1
print("="*20+"\n")

# metode while loop
print("metode while loop")
count = 1
while True:
    print("+"*count)
    count += 1
    if count > sisi:
        break
print("="*20+"\n")

# hanya bilangan ganjil
print("hanya bilangan ganjil")
count = 1
while True:
    if (count%2):
        print("+"*count)
        count += 1
    else :
        count += 1

    if count > sisi:
        break
print("="*20+"\n")

# segitiga bilangan ganjil
print("segitiga bilangan ganjil")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi + "+"*count)
        spasi -= 1
        count += 1
    else :
        count += 1

    if count > sisi:
        break
print("="*20+"\n")





