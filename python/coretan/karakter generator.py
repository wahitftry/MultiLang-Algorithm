import random


# Fungsi untuk mengacak bilangan bulat
def acak_bulat(batas_bawah, batas_atas):
    return random.randint(batas_bawah, batas_atas)


# Fungsi untuk mengacak bilangan float
def acak_float(batas_bawah, batas_atas):
    return random.uniform(batas_bawah, batas_atas)


# Fungsi untuk mengacak elemen dari sebuah list
def acak_list(daftar):
    return random.choice(daftar)


# Fungsi untuk mengacak karakter dari sebuah string
def acak_karakter(string):
    return random.choice(string)


# Fungsi untuk mengacak urutan elemen dari sebuah list
def acak_urutan(daftar):
    random.shuffle(daftar)
    return daftar


# Fungsi untuk mengacak password
def acak_password(panjang):
    karakter = (
        "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    )
    password = "".join(random.sample(karakter, panjang))
    return password


# Contoh penggunaan fungsi-fungsi di atas
print(acak_bulat(1, 10))
print(acak_float(1.0, 10.0))
print(acak_list([1, 2, 3, 4, 5]))
print(acak_karakter("abcdefghijklmnopqrstuvwxyz"))
print(acak_urutan([1, 2, 3, 4, 5]))
print(acak_password(8))
