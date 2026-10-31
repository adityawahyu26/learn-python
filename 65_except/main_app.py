# try dan exception dalam python
# try akan menjalankan dulu programnya
# except akan dijalankan jika dalam running program terdapat error
import os

# membuat loop untuk program angka / 10
while True:
    os.system("cls")
    print(f"{"PROGRAM ANGKA / 10":^20}")
    print("="*22,"\n")
    # try atau mencoba dulu menjalankan ambil input dari user
    try : 
        angka = int(input("Masukkan angka = "))
        hasil = 10/angka 
        print("hasilnya adalah = ", hasil)
    # jika ada value error maka akan menjalankan except
    except:
        print("\nmasukkan input yang valid!")
    # confirm untuk melanjutkan atau menghentikan loop
    confirm = input("Ingin melanjutkan perhitungan (y/n): ")
    if confirm == "n":
        break

print(f"\n\n{"PROGRAM READ & WRITE FILE":^20}")
print("="*26,"\n")
# mencoba menjalankan program dulu
try :
    # membaca file external
    with open("text_1.txt","r") as file:
        read = file.read()
        print(read)
# jika tidak ada file external masuk ke except
except:
        # membuat dulu file externalnya
        with open("text_1.txt","w",encoding='utf-8') as file:
            write = file.write("hello world")
        with open("text_1.txt","a",encoding='utf-8') as file:
            write = file.write("\nhello master")

# akhir dari program
print("\nEND OF PROGRAM")

