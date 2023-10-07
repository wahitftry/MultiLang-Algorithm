# inheritance memiliki fungsi yang relevance antara parent class dan child class


# Parent Class
class Animal:
    def __init__(self):
        self.tipe = "Animal"
        self.kecepatan = "Lambat"

    @staticmethod
    def grow():
        print("Mamalia ini bertumbuh...")


# Child Class
class Cat(Animal):
    def __init__(self, nama, tipe):
        super().__init__()

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"kucing {self.tipe} ini berlari...")


kinoko = Cat(nama="kinoko", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(kinoko.kecepatan)
print(kinoko.tipe)

kinoko.run()
minto.grow()
