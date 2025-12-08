# self adalah representasi dari object itu sendiri di dalam sebuah class di Python.

# Lebih sederhana lagi:

# 🟦 Self = object yang sedang digunakan / diproses

# Dalam Java, ini sama dengan this.

class User:

    def __init__(self, name, merk):
        self.name = name  # menyimpan name ke object
        self.merk = merk

# Self untuk memanggil method lain dalam class    
    
    def start(self):
        print(f"{self.merk} sedang dinyalakan...")

    def jalan(self):
        self.start()   # memanggil method start
        print(f"{self.merk} mulai berjalan.")

user1 = User("Acep","testing")
print(user1.name)  # Acep

user1.jalan()

