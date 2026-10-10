# penulisan string yang benar

# 1. menggunakan tanda kutip "" '' 
# jika pakai " akhiri dengan "
# jika pakai ' akhiri dengan '
print("hari senin") # string biasa menggunakan ""
print('"halo ada yang bisa dibantu?"') # untuk bikin dialog
print('hari jum\'at') # pakai \' biar ' bisa dipakai di ''

# 2. menggunakan backslash \
# mwmanggil beberapa tools yan punya fungsi berbeda
print("==========================")
print("baris satu\nbaris dua") # bikin baris baru
print("warna merah\twarna biru") # bikin jadi jauhan
print("mie ayam\rnasi goreng") # ambil data kedua
print("bandung \bsurabaya") # backspace / hapus satu char

# 3. raw dan multiline string
# raw untuk string yang punya karakter khusus
# multiline untuk bikin string beberapa baris
print("==========================")
print(r"localhost\project\index.php")
print("""
Nama: Aditya
Kota: Surakarta
        """)
print("==========================")
print(r"""
Nama: Aditya
Kota: Surakarta
Dir : localhost/index.php\
        """)


