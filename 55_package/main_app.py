# mengimport package yang terdapat module didalamnya
# package adalah foldernya sedangkan module adalah file py lain yang ingin kita import
from planet import mercury as mc
# menguji coba apa pycache membuat waktu eksekusi menjadi lebih cepat
import time

t_start = time.time()
hasil_tambah = mc.tambah(26,12)
print(hasil_tambah)
t_end = time.time()

print(f"waktu eksekusi adalah: {t_end - t_start}")




