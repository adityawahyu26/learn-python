# **kwargs pada function
# menerima input user yang berupa key=value
# jika user mengirim key=value **kwargs yang menerimanya
# kwargs["key"] = value
# berbentuk dictionary / array assosiatif

# function dengan kwargs / keyword argument
def archon(**kwargs):
    # inisiasi kwargs
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"namanya adalah {nama}, tingginya {tinggi}cm dan berat badannya {berat}kg")

# disini input menyertakan key=value
archon(nama="anastasya",tinggi=175,berat=60)

# menggabungkan dengan *args
def operasi_math(*args,**kwargs):
    # inisiasi **kwargs
    operator = kwargs.get("operator")
    # percabangan untuk melakukan operasi aritmatika sederhana
    if operator == "+":
        count = 0
        for angka in args:
            count += angka
        return count
    elif operator == "*":
        count = 1
        for angka in args:
            count *= angka
        return count
    else:
        return ("masukkan input yang valid")

# user memasukkan funct(args..., key=value)
print(operasi_math(1,2,3,4,5,6,7,8,9,operator="+"))
print(operasi_math(1,2,3,4,5,6,7,8,9,operator="*"))