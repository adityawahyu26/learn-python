# format string

# string
name = "aditya"
format_str = f"hi, good afternoon {name}."
print(format_str)

# float
data = 125.0
format_str = f"float : {data}"
print(format_str)

# angka
data = 26
format_str = f"angka : {data}"
print(format_str)

# boolean
data = True
format_str = f"boolean : {data}"
print(format_str)

# bilangan bulat
data = 12
format_str = f"bilangan bulat : {data:d}"
print(format_str)

# bilangan dengan ordo ribuan
data = 2000000
format_str = f"bilangan jutaan : {data:,}"
print(format_str)

# bilangan desimal
data = 26.53984
format_str = f"bilangan desimal : {data:.2f}"
print(format_str)

# menampilkan leading zero
data = 26.53984
format_str = f"leading zero : {data:06.2f}"
print(format_str)

# menampilakan tanda + atau -
data_negatif = -10
data_positif = 10.832834
format_negatif = f"bilangan negatif : {data_negatif:-}"
format_positif = f"bilangan positif : {data_positif:+.3f}"
print(format_negatif)
print(format_positif)

# memformat persen
data_persen = 0.026
format_persen = f"angka persen : {data_persen:.2%}"
print(format_persen)

# operasi aritmatika di placeholder
harga = 12000
mie_ayam = 6
total_belanja = f"Total Belanja : Rp {harga*mie_ayam:,}"
print(total_belanja)

# format angka lain (binary, octal, hexadecimal)
angka = 26
format_binary = f"angka binary : {bin(angka)}"
format_octal = f"angka octal : {oct(angka)}"
format_hex = f"angka hex : {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)




