# default argument dalam function
# function(argument=default)
# default argument muncul ketika argument tidak diisi

def hallo(nama="admin"):
    print(f"hallo, selamat datang {nama}!")

hallo("aditya")
hallo()

def sayHi(nama,sapaan="selamat pagi"):
    print(f"{sapaan}, {nama}!")

sayHi("aditya","selamat malam")
sayHi("aditya")

def kuadrat(angka=5,kuadrat=2):
    hasil = angka**kuadrat
    return hasil

print(kuadrat())
print(kuadrat(kuadrat=3,angka=2))

def angka(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(angka())
print(angka(input1=2,input3=4))


