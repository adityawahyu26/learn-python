# __main__ adalah hasil dari var __name__ pada file py yang sedang di jalankan
# __name__ pada module yang diimport ga akan menghasilkan __main__ tapi nama modulenya

# jika menjalankan program ini, __name__ = __main__
print(f"ini adalah __name__ pada file aktif = {__name__}")

# di module import jika di run disini, maka punya nya akan __name__ = namamodule
import venus

# ini tidak akan menampilkan __main__.py, pakai python package / python -m package
import package

# ini case yang paling banyak, jika perintah tertentu tidak langsung dirun diimport
# misal ada perintah penting atau top level code environment tertentu
# maka walaupun import kode ini maka tetap saja akses ke perintah itu akan dilarang
# jadi harus benar-benar run program ini, bukan sekedar import
if __name__ == "__main__":
    def tambah(a:int,b:int)->int:
        return a + b



