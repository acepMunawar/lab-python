# 

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @classmethod
    def from_text(cls, text):
        brand, color = text.split("-")
        return cls(brand, color)   # memanggil constructor utama
    
    @classmethod
    def sparepart(cls):
        return cls("hello class method","testing")
    
car = Car.from_text("Toyota-Black")
print(car.brand, car.color)

car_sparepart = Car.sparepart()
print(car_sparepart)