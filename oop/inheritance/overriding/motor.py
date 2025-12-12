from kendaraan import kendaraan

class Motor(kendaraan):

    def klakson(self):
        print(f"Motor {self.info()} memiliki klakson")

    def nyalakan(self):
        print(f"{self.merek} dinyalakan secara otomatis")
