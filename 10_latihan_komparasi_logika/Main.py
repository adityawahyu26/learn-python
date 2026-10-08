# case 1 : kurang dari 3 atau lebih dari 10 untuk true
# +++ 3 --- 10 +++
# + : true, - : false
angka = int(input("Masukkan angka kurang dari 3 \natau lebih dari 10: "))

isKurangDari3 = angka < 3
isLebihDari10 = angka > 10
isCorrect = isKurangDari3 or isLebihDari10
print(f"Apa {angka} kurang dari 3 / lebih dari 10?\n: {isCorrect}")

print("\n=========\n")

# case 2 : lebih dari 3 dan kurang dari 10 untuk true
# --- 3 +++ 10 ---
# + : true, - : false
angka = int(input("Masukkan angka lebih dari 3 \ndan kurang dari 10: "))
isLebihDari3 = angka > 3
isKurangDari10 = angka < 10
isCorrect = isLebihDari3 and isKurangDari10
print(f"Apa {angka} lebih dari 3 & kurang dari 10?\n: {isCorrect}")