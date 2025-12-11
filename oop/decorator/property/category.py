class Category:
    _name = ""

    @property
    def name(self):
        return self._name
    

    def name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self._name = name

category = Category()
category.name = "Laptop"
print(category.name)