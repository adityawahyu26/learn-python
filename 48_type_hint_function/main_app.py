# type hint pada function
# mengatur tipe data yang diterima function
# dan menentukan tipe data return dari function

# function ini menerima input int dan return int 
def kuadrat(input_angka:int) -> int:
    hasil = input_angka**2
    return hasil

y = kuadrat(26)
print(y)

# function ini menerima input float dan int, serta return float
def total_harga(input_harga:float,jumlah_barang:int) -> float:
    return input_harga*jumlah_barang

x = total_harga(10.0,6)
print(x)




