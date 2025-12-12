class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        return f"Merek: {self.merek}, Tahun: {self.tahun}"
    
    def nyalakan(self):
        print(f"{self.merek} dinyalakan")