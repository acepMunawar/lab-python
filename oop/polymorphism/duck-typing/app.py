from mobil import Mobil
from motor import Motor
from perahu import Perahu

# Function yang polymorphic (duck typing)
def operasikan_kendaraan(kendaraan):
    kendaraan.start()   # kendaraan = objek apa saja yg punya .start()

def main():
    # Membuat list berbagai objek kendaraan
    kendaraan_list = [
        Mobil(),
        Motor(),
        Perahu()
    ]

    # Loop dan jalankan
    for kendaraan in kendaraan_list:
        operasikan_kendaraan(kendaraan)

if __name__ == "__main__":
    main()
    