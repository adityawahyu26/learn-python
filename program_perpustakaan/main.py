# program database perpustakaan
import os
import CRUD as CRUD

# cek apa dijalankan di file utama
if __name__ == "__main__":
    # mengecek dan menyimpan jenis sistem operasi
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix":os.system("clear")
        case "nt":os.system("cls")
        
    print("SELAMAT DATANG!")
    print("PROGRAM DATABASE PERPUSTAKAAN")
    print("==============================\n")

    CRUD.innit_console()

    # menggunakan loop untuk run programnya
    while(True):
        # bergantung os, membuat terminal lebih clear
        match sistem_operasi:
            case "posix":os.system("clear")
            case "nt":os.system("cls")
        
        print("SELAMAT DATANG!")
        print("PROGRAM DATABASE PERPUSTAKAAN")
        print("==============================\n")

        print("1. Read")
        print("2. Add")
        print("3. Update")
        print("4. Delete")

        # ambil input user
        user_option = input("\nmasukan opsi yang dipilih: ")

        # mencocokan input user dengan beberapa case
        match user_option:
            case "1":CRUD.read_data()
            case "2":CRUD.create_data()
            case "3":print("UPDATE DATA")
            case "4":print("DELETE DATA")

        # membuat option untuk melanjutkan / menghentikan program
        confirm = input("apa anda ingin keluar dari program (y/n): ")
        if confirm == "y" or confirm == "Y":
            break

print("\n[END OF PROGRAM]")
