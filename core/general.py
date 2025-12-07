# Initialisation
# Python tidak punya keyword khusus (seperti null di java)

# None -> default paling umum (seperti null)

data = None

# basic type

count = 0
text = ""
items = []
user = {}
is_active = False

# type data

#====================== Integer

x_int = 10
y_int = -5
z_int = 1_000_000 #bisa pakai underscroe untuk ribuan

print(type(x_int), x_int)
print(type(z_int), z_int)

#====================== Float

pi = 3.14159
gaji = 12.5

print(type(pi), pi)

#====================== Decimal

from decimal import Decimal

harga = Decimal("10.50")
ppn = Decimal("0.10")
total = harga + harga * ppn

print(type(total), total)

#====================== Boolean

is_active = True
is_deleted = False

print(type(is_active), is_active)
