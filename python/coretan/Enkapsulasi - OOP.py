# Encapsulation untuk mencegah terjadi perubahan yang di sengaja atau tidak di sengaja


class Mobil:
    def __init__(self, plat):
        self._plat = plat
        self._tipe = "Avanza"
        self._bensin = 40  # liter

    # getter
    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self._bensin} liter")

    # setter
    def aturMaksimumBensin(self, bensin):
        self._bensin = bensin


avanza = Mobil(plat="B 1234 AC")

# print(avanza._plat)

# print(avanza._tipe)

# print(avanza._bensin)

avanza._bensin = 30
print(avanza._bensin)

avanza.lihatMaksimumBensin()
avanza.aturMaksimumBensin(50)
avanza.lihatMaksimumBensin()
