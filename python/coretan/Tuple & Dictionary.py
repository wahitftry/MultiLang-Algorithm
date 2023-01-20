print("======TUPLE======")

tuple1 = ("apple", "banana", "watermelon")
tuple2 = (1, 3, 7, 9, 10)
tuple3 = (True, False, False)
tuple4 = ("abc", 10, True, 40, "male")

fruit_taple = ("apple", "banana", "watermelon", "orange", "mango")

print(fruit_taple[-2:])

print("\n======DICTIONARY======")
print("===[key1:value1, key2:value2]===")

fruit_dict = {
    "nama": "pisang",
    "jenis": "ambon",
    "kode": 891,
    "harga": 20000,
}

print(fruit_dict["jenis"])

fruit_dict["nama"] = "jeruk"

fruit_dict["harga"] = 25000

for key, value in fruit_dict.items():
    print(key, value)

for key in fruit_dict.keys():
    print(key, fruit_dict[key])

print("\n======BONUS======")
print("===SET===")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)

print(A & B)

print(A - B)
print(B - A)

print(A ^ B)
