# import dalam python 
# untuk menggunakan file py eksternal lain

# mengimport source code dari test1.py
import test1
# mengimport source yang punya data seperti variable
import variable
# mengimport source yang punya funct di dalamnya
import funct

# menggunakan var dari import dengan mencantumkan sourcenya
# var = filepyimport.varimport
hasil_data = variable.data
print(hasil_data)

# menggunakan funct dari import dengan mencantumkan sourcenya
# var = filepyimport.functimport
math = funct.kuadrat(6)
print(math)