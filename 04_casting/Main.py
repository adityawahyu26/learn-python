# casting adalah merubah tipe data ke tipe data lainnya

# casting dari tipe data integer ke tipe data lainnya
print ("==== INTEGER ====")
data_int = 12
print ("data = ", data_int, ", type =", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) 
# akan false jika 0, selain itu true baik itu postif / negatif
print ("data = ", data_float, ", type =", type(data_float))
print ("data = ", data_str, ", type =", type(data_str))
print ("data = ", data_bool, ", type =", type(data_bool))

# casting dari tipe data string ke tipe data lainnya
print ("==== STRING ====")
data_str = "10"
print ("data = ", data_str, ", type =", type(data_str))
data_int = int(data_str)
data_float = float(data_str)    
data_bool = bool(data_str)
# untuk bool akan false jika string kosong, selain itu true
print ("data = ", data_int, ", type =", type(data_int))
print ("data = ", data_float, ", type =", type(data_float))
print ("data = ", data_bool, ", type =", type(data_bool))

# casting dari tipe data float ke tipe data lainnya
print ("==== FLOAT ====")
data_float = 9.5
print ("data = ", data_float, ", type =", type(data_float))
data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika 0.0 / 0
print ("data = ", data_int, ", type =", type(data_int))
print ("data = ", data_str, ", type =", type(data_str))
print ("data = ", data_bool, ", type =", type(data_bool))

# casting dari tipe data boolean ke tipe data lainnya
print ("==== BOOLEAN ====")
data_bool = False
print ("data = ", data_bool, ", type =", type(data_bool))
data_int = int(data_bool) # akan 1 jika true, 0 jika false
data_str = str(data_bool)
data_float = float(data_bool) 
# akan 1.0 jika true, 0.0 jika false
print ("data = ", data_int, ", type =", type(data_int))
print ("data = ", data_str, ", type =", type(data_str))
print ("data = ", data_float, ", type =", type(data_float))

