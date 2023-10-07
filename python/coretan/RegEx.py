print("=====RegEx=====")

import re

print("\n=====MATCH RegEx=====")
teks = "regex"
x = re.match("^r...x$", teks)
print(x)

print("\n=====SPLIT RegEx=====")
teks = "i'm happy learn regex"
x = re.split(r"\s", teks)
print(x)

print("\n=====SUB RegEx=====")
teks = """
        the 3 loop type in language python programming are while loop,
        for loop and nested loop 2022
        """
x = re.sub(r"\d+", "", teks)
print(x)

print("\n=====SEARCH RegEx=====")
teks = "hujan deras di kawasan depok"
result = re.search("^hujan.*depok$", teks)

if result:
    print("YES! we have a match.")
else:
    print("No match.")

print("\n=====FINDALL RegEx=====")
teks = "23 oct 2019 23 oct,2019 23 october,2019 oct 26,2020"
x = re.findall(r"\d{2} [a-z]{3} \d{4}", teks)
print(x)

print("\n=====SUB RegEx=====")
teks = "Harga 1 mobil antik tersebut yaitu $1000"
x = re.sub(r"\$\d+", "_", teks)
print(x)

print("\n=====SUB RegEx=====")
teks = "Akan dialihkan ke http://medium.com"
x = re.sub(r"http[s]?\://\S+", "_", teks)
print(x)

print("\n=====FINDALL RegEx=====")
teks = "Luar biasa! Banyak anak-anak muda traveling tahun ini, begini tanggapan lesti"
x = re.findall
print(x)
