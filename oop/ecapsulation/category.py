class Category:
    _name = ""
    # sama dngan private String name; di java
    # di python kita hanya menandai menggunakan underscore di belakang identifier 
    # walaupun tidak bersifat private dan masih bisa di akses

    def set_name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self._name = name

    def get_name(self):
        return self._name
    
category1 = Category()
category1.set_name("Gadge")

print(category1.get_name())