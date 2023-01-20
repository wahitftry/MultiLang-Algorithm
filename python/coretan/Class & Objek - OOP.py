class Cat:
    """
    ini adalah class untuk membuat objek kucing
    melalui kelas ini ktia bisa mendefinisikan nama dan juga tipe dari kucing yang dibuat
    """

    spesies = "kucing"

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self, speed):
        print(f"kucing {self.nama} berlari dengan {speed}...")

    def play(self):
        print(f"kucing {self.nama} bermain dengan kucing lainnya...")

    def eat(self):
        pass


# Membuat Objek
kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(f"kinako adalah seekor {kinako.__class__.spesies}")
print(f"{kinako.nama} adalah kucing jenis {kinako.tipe}")
print(f"{minto.nama} adalah kucing jenis {minto.tipe}")

# print(kinako.nama)
# print(minto.tipe)
kinako.run("cepat")
kinako.play()

print(kinako.__doc__)

# Abstact Object (untuk AI)
class RandomForest:
    pass
