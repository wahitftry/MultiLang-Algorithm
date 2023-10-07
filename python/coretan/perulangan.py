print("=====LOOP=====")
print("===WHILE LOOP===")

count = 0

while count < 9:
    print("Nilai count:", count)
    count = count + 1

print("selamat berjuang!")

print("\n===FOR LOOP===")

list_angka = [1, 2, 3, 4, 5]

for x in list_angka:
    print("intruksi berjalan...")
    print(x)

print(range(10))

list_range = list(range(10))
print(list_range)

for x in list(range(2, 20, 3)):
    print(x)

for x in list(range(1, 11)):
    print(x)

print("\n===NESTED LOOP===")

i = 90

while i < 100:
    j = 2
    print((i / j))
    while j < +(i / j):
        print("loop dalam loop!")
        j = j + 1
        i = i + 1

print("Selamat Berjuang")

print("\n===BREAK & CONTINUE===")

for val in "string":
    if val == "g":
        continue

    print(val)

for val in "string":
    if val == "i":
        break

    print(val)

print("loop telah berakhir.")

print("\n===FOR ELSE===")

daftar_murid = ["Angga", "Mardadi", "Rowi"]

nama_murid = "Jaka"

for nama in daftar_murid:
    if nama == nama_murid:
        print((nama))
        break

else:
    print("nama murid tidak ditemukan")

daftar_murid = ["Angga", "Mardadi", "Rowi"]

nama_murid = "Angga"

for nama in daftar_murid:
    if nama == nama_murid:
        print((nama))
        break

else:
    print("nama murid tidak ditemukan")

if daftar_murid == 0:
    # implementation for the first branch
    print("No students in the list")

else:
    # implementation for the second branch (same as the third branch)
    print("There are students in the list")
