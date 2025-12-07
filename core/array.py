# ========================= List

buah = ["apel","mangga","jeruk"]

buah.append("pisang")
buah[1] = "melon"
buah.remove("jeruk")

# len() untuk menampilkan size array
print(len(buah))

for i in buah:
    print(i)

# ========================= Tuple
# Array yang tidak bisa di ubah (immutable)

koordinat = (20, 40)

print(koordinat[0])

# ========================= Disct
# Array assosiatif (key-value)

data = {
    "name":"Acep",
    "umur": 31
}

print(data["name"])

# ========================= Set
# Set adalah kumpulan data yang tidak berurut, tidak memiliki index, 
# dan semua element nya unik(tidak boleh duplikat)

car_type = {"toyota","mitsubishi","honda","honda"}

print(car_type)