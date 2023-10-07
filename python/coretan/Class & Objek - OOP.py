class Car:
    """
    Ini adalah class untuk membuat objek mobil
    """

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def start(self):
        print(
            f"{self.brand} {self.model} ({self.year}) dengan warna {self.color} dinyalakan mesinnya."
        )

    def stop(self):
        print(
            f"{self.brand} {self.model} ({self.year}) dengan warna {self.color} dimatikan mesinnya."
        )

    def accelerate(self, speed):
        self.speed += speed
        print(
            f"{self.brand} {self.model} ({self.year}) dengan warna {self.color} dipercepat menjadi {self.speed} km/jam."
        )

    def brake(self, speed):
        self.speed -= speed
        if self.speed < 0:
            self.speed = 0
        print(
            f"{self.brand} {self.model} ({self.year}) dengan warna {self.color} diperlambat menjadi {self.speed} km/jam."
        )


# Membuat objek mobil
car1 = Car(brand="Toyota", model="Avanza", year=2015, color="silver")
car2 = Car(brand="Honda", model="Jazz", year=2018, color="red")

# Memanggil method pada objek mobil
car1.start()
car1.accelerate(50)
car1.accelerate(30)
car1.brake(20)
car1.stop()

car2.start()
car2.accelerate(70)
car2.brake(10)
car2.brake(100)
car2.stop()
