# operator assignment =

# operator assignment +=
a = 26
print("------ operator assignment += ---")
print("nilai awal :", a)
print("+= 6")
a += 6
print("hasil dari +=", a)

# operator assignment -=
a = 26
print("------ operator assignment -= ---")
print("nilai awal :", a)
print("-= 7")
a -= 7
print("hasil dari -=", a)

# operator assignment *=
a = 26
print("------ operator assignment *= ---")
print("nilai awal :", a)
print("*= 8")
a *= 8
print("hasil dari *=", a)

# operator assignment /=
a = 26
print("------ operator assignment /= ---")
print("nilai awal :", a)
print("/= 9")
a /= 9
print("hasil dari /=", a)

# operator assignment %=
a = 26
print("------ operator assignment %= ---")
print("nilai awal :", a)
print("%= 10")
a %= 10
print("hasil dari %=", a)

# operator assignment //=
a = 26
print("------ operator assignment //= ---")
print("nilai awal :", a)
print("//= 11")
a //= 11
print("hasil dari //=", a)

# ========================
# operator assignment pada bitwise
# bitwise OR
print("\n------ operator assignment |= ---")
c =  True
print("nilai awal :", c)
c|= False
print("hasil dari |= false :", c)
c =  False
print("nilai awal :", c)
c |= False
print("hasil dari |= false :", c)

# bitwise AND
print("\n------ operator assignment &= ---")
c =  True
print("nilai awal :", c)
c &= True
print("hasil dari &= true :", c)
c =  True
print("nilai awal :", c)
c &= False
print("hasil dari &= false :", c)

# bitwise XOR
print("\n------ operator assignment ^= ---")
c =  True
print("nilai awal :", c)
c ^= False
print("hasil dari ^= False :", c)
c =  True
print("nilai awal :", c)
c ^= True
print("hasil dari ^= true :", c)

# bitwise right shift
print("\n------ operator assignment >>= ---")
d =  0b00100100
print("nilai awal :", format(d, "08b"))
d >>= 2
print("hasil dari >>= 2 :", format(d, "08b"))

# bitwise left shift
print("\n------ operator assignment <<= ---")
d =  0b00100100
print("nilai awal :", format(d, "08b"))
d <<= 2
print("hasil dari <<= 2 :", format(d, "08b"))









