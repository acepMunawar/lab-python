
# __init__ sama dengan constructor yang ada di dalam java

class Car:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    
    def greet(self):
        print(f"Halo, nama saya {self.name}, usia {self.age} tahun!")

car = Car("Acep", 30)
car.greet()
