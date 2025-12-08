#======================== Class
# Class adalah blueprint atau template untuk membuat object.
# Analogi:
# Class itu seperti cetakan kue. Cetakan menentukan bentuk dan sifat kue, tapi bukan kuenya sendiri.

class Car:

    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def jalan(self):
        print(f"{self.merk} berwarna {self.warna} sedang berjalan.")

car_toyota = Car("Toyota","Green")
car_honda = Car("Honda","White")

car_toyota.jalan()
car_honda.jalan()
