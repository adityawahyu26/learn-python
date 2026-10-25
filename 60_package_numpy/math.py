# package numpy dalam python
# digunakan untuk perhitungan matematika dan data science

# import package numpy
import numpy as np

# menggunakan list biasa, ada koma disetiap valuenya
list_a = [1,2,3,4,5]
print(f"list a = {list_a}")
# tidak bisa melakukan operasi aritmatika untuk setiap valuenya
# print(f"list a ^2 = {list_a**2}")
# print(f"list a *5 = {list_a*5}")

# membuat vector dari numpy, valuenya tidak mengandung koma
vector_a = np.array([1,2,3,4,5])
print(f"\nvector a = {vector_a}")
# bisa melakukan operasi aritmatika untuk setiap value
print(f"vector a ^2 = {vector_a**2}")
print(f"vector a *5 = {vector_a*5}")

# membuat matrix dengan numpy
matrix_a = np.array([(1,2,3),(4,5,6)])
print(f"\nmatrix a =\n{matrix_a}")
# melakukan operasi aritmatika untuk setiap value di dalam matrix
print(f"matrix a ^2 =\n{matrix_a**2}")
print(f"matrix a *5 =\n{matrix_a*5}")

# membuat matrix yang hanya berisi angka 0, [jml kelompok, jml value per kelompok]
zeros_a = np.zeros([2,3])
print(f"\nzeros a =\n{zeros_a}")

# membuat matrix yang hanya berisi angka 1, [jml kelompok, jml value per kelompok]
ones_a = np.ones([2,3])
print(f"\nones a =\n{ones_a}")

# melakukan gabungan operasi aritmatika pada matrix, matrix berpangkat, matrix ones
result = matrix_a + matrix_a**2 + ones_a
print(f"\nmatrix a + matrix a**2 + ones a =\n{result}")