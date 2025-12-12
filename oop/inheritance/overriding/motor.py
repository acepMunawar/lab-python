from kendaraan import Kendaraan

class Motor(Kendaraan):

    def klakson(self):
        print(f"Motor {self.info()} memiliki klakson")

# Overriding
    def nyalakan(self):
        print(f"{self.merek} dinyalakan secara otomatis")
