print("=====FUNCTION=====")
print("===Non-Paramater Function===")


def hello_world():
    var = "Halo Wahit, hello world!"
    print(var)


hello_world()
print("\n===Paramater Function===")


def selamat_datang(nama):
    var = f"halo {nama}, welcome!"
    print(var)


selamat_datang("wahit")


def selamat_datang_dari(nama, asal):
    var = f"Halo {nama} dari {asal}, welcome!"
    print(var)


selamat_datang_dari("Wahit", "Gondang Slamet")
selamat_datang_dari(asal="Klaten", nama="Efi")


def selamat_datang_all(*daftar_nama):
    var = "halo"
    for nama in daftar_nama:
        var += " " + nama + ","
    var += " welcome!"
    print(var)


selamat_datang_all("efi", "arthur", "shindu", "andi", "rowi")
print("\n===Anonim Function===")
double = lambda x: x * 2
print(double(7))


def selamat_datang(nama):
    """
    ini adalah fungsi untuk menyapa
    nama yang telah disebutkan
    """
    var = f"Halo {nama}, welcome!"
    print(var)


selamat_datang("efi")
print(selamat_datang.__doc__)

x = 100


def operasi(a, b, c):
    op1 = a + b
    op2 = op1 // c
    print("a di dalam function:", a)
    print("b di dalam function:", b)
    print(x)
    return op2


a = 2
b = 1
hasil = operasi(a=10, b=5, c=3)
print(hasil)

print("a di luar function:", a)
print("b di luar function:", b)
