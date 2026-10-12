# simple calc dengan if else dan elif statement

print("="*10)
print("Simple Calc")
print("="*10 + "\n")

angka1 = float(input("masukkan angka 1: "))
operator = input("Masukkan Operator(+,-,*,/): ")
angka2 = float(input("masukkan angka 2: "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah: {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah: {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"hasilnya adalah: {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasilnya adalah: {hasil}")
else:
    print("Masukkan input yang valid!")

