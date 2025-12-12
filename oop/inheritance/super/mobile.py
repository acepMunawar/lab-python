from kendaraan import kendaraan

class Mobil(kendaraan):

    def __init__(self, merek, tahun, jumlah_roda):
        super().__init__(merek, tahun)
        self.jumlah_roda = jumlah_roda


    def klakson(self):
        print(f"Mobile {self.info()} memiliki klaskson")

