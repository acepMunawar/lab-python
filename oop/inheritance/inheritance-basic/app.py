from mobile import Mobil
from motor import Motor

class App:
    def __init__(self):
        self.avanza = Mobil("Avanza", 2019)
        self.scoopy = Motor("Scoopy", 2022)

    def run(self):
        self.avanza.nyalakan()
        self.avanza.klakson()
        self.scoopy.nyalakan()
        self.scoopy.klakson()
if __name__ == "__main__":
    app = App()
    app.run()