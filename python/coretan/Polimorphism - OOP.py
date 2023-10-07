# bisa menjalankan fungsi yang sama dari objek yang berbeda
class Cat:
    def __init__(self):
        self.nama = "Meong"
        self.tipe = "Anggora"

    @staticmethod
    def forward():
        print("Kucing berlari...")


class Bird:
    def __init__(self):
        self.nama = "Erago"
        self.tipe = "Elang"

    @staticmethod
    def forward():
        print("Burung terbang...")


def melaju(objek):
    objek.forward()


meong = Cat()
erago = Bird()

melaju(meong)
melaju(erago)
