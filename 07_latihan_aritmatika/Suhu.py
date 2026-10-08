# === Latihan Konversi Temperatur ===

# mengambil input dari user dalam bentuk celcius
celcius = float(input("Masukkan suhu dalam Celcius: "))

# konversi ke Reamur
reamur = (4/5) * celcius

# konversi ke Fahrenheit
fahrenheit = ((9/5) * celcius) + 32

# konversi ke Kelvin
kelvin = celcius + 273.15

# menampilkan suhu dan hasil konversinya
print("\nHasil Konversi Suhu:")
print(f"Suhu dalam Celcius: {celcius} °C")
print(f"Suhu dalam Reamur: {reamur} °R")
print(f"Suhu dalam Fahrenheit: {fahrenheit} °F")
print(f"Suhu dalam Kelvin: {kelvin} K\n")