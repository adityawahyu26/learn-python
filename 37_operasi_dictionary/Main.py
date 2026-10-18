# operasi dictionary
data_dict = {
    "ven":"venti",
    "zho":"zhongli",
    "rai":"raiden ei",
    "nah":"nahida",
    "fur":"furina",
    "mav":"mavuika",
    "col":"columbina",
    "tsa":"tsaritsa"
}

# mengecek panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dari dictionary = {LENDICT}")

# mengecek apa key ada di dictionary
KEY = "fur"
CHECKKEY = KEY in data_dict
print(f"apa {KEY} ada di dalam data_dict = {CHECKKEY}")

# mengakses data dengan GET
print(data_dict.get("mav","data tidak ditemukan"))
# bisa membuat message custom sendiri
print(data_dict.get("noy","data tidak ditemukan"))

# mengupdate data di dictionary
data_dict.update({"ven":"venti"})
# akan otomatis di add jika belum ada
data_dict.update({"neu":"neuvilette"})
print(data_dict)

# menghapus data dari dalam dictionary
del data_dict["neu"]
print(data_dict)



