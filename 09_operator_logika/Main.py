# operator logika atau boolean

# NOT !, selalu membalik nilai boolean
a = True
b = False
not_a = not a
not_b = not b
print("=== NOT ===")
print("a =", a, "-> not a =", not_a)
print("b =", b, "-> not b =", not_b)

# AND &&, harus bernilai True semua untuk hasil true
print("\n=== AND ===")
a = True
b = True
and_ab = a and b
print(a, "AND", b, "=", and_ab)
a = True
b = False
and_ab = a and b
print(a, "AND", b, "=", and_ab)
a = False
b = True    
and_ab = a and b
print(a, "AND", b, "=", and_ab)
a = False
b = False
and_ab = a and b
print(a, "AND", b, "=", and_ab)

# OR ||, cukup salah satu bernilai True untuk hasil true
print("\n=== OR ===")
a = True
b = True
or_ab = a or b
print(a, "OR", b, "=", or_ab)
a = True
b = False
or_ab = a or b
print(a, "OR", b, "=", or_ab)
a = False
b = True    
or_ab = a or b
print(a, "OR", b, "=", or_ab)
a = False
b = False
or_ab = a or b
print(a, "OR", b, "=", or_ab)

# XOR, kedua input harus berbeda untuk hasil true
print("\n=== XOR ===")
a = True
b = True
xor_ab = a ^ b
print(a, "XOR", b, "=", xor_ab)
a = True
b = False
xor_ab = a ^ b
print(a, "XOR", b, "=", xor_ab)
a = False
b = True    
xor_ab = a ^ b
print(a, "XOR", b, "=", xor_ab)
a = False
b = False
xor_ab = a ^ b
print(a, "XOR", b, "=", xor_ab)

