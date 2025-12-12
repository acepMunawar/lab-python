from mobile import Mobil
from motor import Motor

class App:
    def __init__(self):
        self.avanza = Mobil("Avanza", 2019, 4)
        self.scoopy = Motor("Scoopy", 2022)

    def run(self):
        self.avanza.nyalakan()
        self.avanza.klakson()
        self.avanza.jumlah_roda
        self.scoopy.nyalakan()
        self.scoopy.klakson()

app = App()
app.run()