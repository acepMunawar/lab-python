
# static method dalam Python adalah method di dalam class yang tidak membutuhkan self atau cls.
# Artinya: method tersebut tidak bergantung pada object dan tidak bergantung pada class.

class User:

    @staticmethod
    def tambah(x, y):
        return x + y

    @staticmethod
    def is_valid_name(name):  # static method
        return len(name) > 0

print(User.is_valid_name("Acep"))  # True (static)
print(User.tambah(5,23))

# 🧠 Kesimpulan:

# Static method = fungsi yang tidak punya akses ke object maupun class
# Dipakai untuk utility/helper
# Didefinisikan dengan @staticmethod
# Tidak butuh self atau cls
# Beda dengan instance method dan class method