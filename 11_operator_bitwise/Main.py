# operator bitwise, operasi binary
#   0 0 0 0 0 0 0 0 // binary
# [ 8 7 6 5 4 3 2 1 ] // index
# 0 0 0 0 0 0 1 0 = 2
#             2*1 = 2
# 0 0 0 0 0 0 0 1 = 1
#               2*0 = 1

# inisiasi variable dan nilanya
a = 9
b = 5

# bitwise OR (|)
# hanya perlu satu input true / 1 untuk output true
c = a | b
print("=== Bitwise OR (|) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("nilai b = ", b, ", binary = ", format(b, '08b'))
print("-------------------------------(|)")
print("nilai c = ", c, ", binary = ", format(c, '08b'))

# bitwise AND (&)
# semuan input harus true / 1 untuk output true
d = a & b
print("\n=== Bitwise AND (&) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("nilai b = ", b, ", binary = ", format(b, '08b'))
print("-------------------------------(&)")
print("nilai d = ", d, ", binary = ", format(d, '08b'))

# bitwise XOR (^)
# kedua input harus berbeda untuk output true
e = a ^ b
print("\n=== Bitwise XOR (^) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("nilai b = ", b, ", binary = ", format(b, '08b'))
print("-------------------------------(^)")
print("nilai d = ", e, ", binary = ", format(e, '08b'))

# bitwise NOT (~)
# selalu membalikkan nilai input ke arah sebaliknya
f = ~a
print("\n=== Bitwise NOT (~) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("-------------------------------(~)")
print("nilai f = ", f, ", binary = ", format(f, '08b'))

# metode flip dengan bitwise XOR (^)
# 0xFF = 1111 1111 
g = 0xFF ^ a
print("\n=== Metode Flip Bitwise XOR (^) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("-------------------------------(^)")
print("nilai g = ", g, ", binary = ", format(g, '08b'))

# bitwise shift left (<<)
# misal 00010010 << 2
# jadi 01001000, ke kiri 2 kali 
h = a << 2
print("\n=== Bitwise Shift Left (<<) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("-------------------------------(<<)")
print("nilai h = ", h, ", binary = ", format(h, '08b'))

# bitwise shift right (>>)
# misal 00100100 >> 2
# jadi 00001001, ke kanan 2 kali 
i = a >> 2
print("\n=== Bitwise Shift Right (>>) ===")
print("nilai a = ", a, ", binary = ", format(a, '08b'))
print("-------------------------------(>>)")
print("nilai i = ", i, ", binary = ", format(i, '08b'))

