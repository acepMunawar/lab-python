class Category:
    __name = ""

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self.__name = name

category = Category()
category.name = "Laptop"
print(category.name)