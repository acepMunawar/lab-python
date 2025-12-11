# Jika ingin cara Pythonic: gunakan @property
# Programmer Python modern jarang pakai setter/getter manual.

class Category:
    __name = ""
    # sama dngan private String name; di java
    # di python kita hanya menandai menggunakan underscore 2 kali di belakang identifier 
    # walaupun tidak bersifat private dan masih bisa di akses

    def set_name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self.__name = name

    def get_name(self):
        return self.__name
    
category1 = Category()
category1.set_name("Gadge")

print(category1.get_name())

# print(category1.__name)
# ini akan error