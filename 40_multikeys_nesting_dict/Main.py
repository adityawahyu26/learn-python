# multi keys dan nesting dictionary
# latihan membuat tabel database

# inisiasi semua dictionary sourcenya
char_1 = {
    "name":"columbina",
    "vision":"hydro",
    "region":"nodkrai"
}

char_2 = {
    "name":"lauma",
    "vision":"dendro",
    "region":"nodkrai"
}

char_3 = {
    "name":"varesa",
    "vision":"electro",
    "region":"natlan"
}

char_4 = {
    "name":"furina",
    "vision":"hydro",
    "region":"fontaine"
}

# gabung menjadi nested dictionary
my_party = {
    "GI001":char_1,
    "GI002":char_2,
    "GI003":char_3,
    "GI004":char_4
}

# buat header tabel databasenya
print(f"{'KEY':<6} {'NAME':<10} {'VISION':<10} {'REGION':<10}")
print("-"*37)

# menggunakan for loop untuk datanya
for chars in my_party:
    KEY = chars

    NAME = my_party[KEY]["name"]
    VISION = my_party[KEY]["vision"]
    REGION = my_party[KEY]["region"]

    print(f"{KEY:<6} {NAME:<10} {VISION:<10} {REGION:<10}")



