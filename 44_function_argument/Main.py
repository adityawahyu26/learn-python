# function dengan argument
# function(argument)

# function dengan argument string
def hello(nama):
    print(f"hallo, selamat datang {nama}")

hello("anastasya")

# function dengan argument untuk operasi aritmatika
def operasiKali(nilai1,nilai2):
    hasil = nilai1 * nilai2
    print(f"{nilai1} * {nilai2} = {hasil}")

operasiKali(23,54)

# function dengan argument untuk for loop list
tamu_undangan = ["bapak kepala sekolah", 
                 "bapak/ibu guru",
                 "bapak/ibu wali murid"]

def sambutan(peserta):
    peserta_acara = peserta.copy()

    for tamu in peserta_acara:
        print(f"kepada yang terhormat, {tamu}")

sambutan(tamu_undangan)

