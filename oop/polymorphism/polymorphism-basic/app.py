from anjing import Anjing
from kucing import Kucing
from sapi import Sapi

class App:
    def __init__(self):
        self.hewan_list = [
            Anjing("Anjing"),
            Kucing("Kucing"),
            Sapi("Sapi")
        ]
    
    def run(self):
        for hewan in self.hewan_list:
            hewan.suara()

if __name__ == "__main__":
    app = App()
    app.run()