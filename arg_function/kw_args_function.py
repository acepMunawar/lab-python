# Function 1: menampilkan nama dan umur
def profile_basic(**kwargs):
    name = kwargs.get("name", "Unknown")  # default jika key tidak ada
    age = kwargs.get("age", 0)
    
    print(f"Nama: {name}, Umur: {age}")

profile_basic(name="Acep", age=28)


# Function 2: menampilkan semua key-value
def profile_verbose(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

profile_verbose(name="Acep", age=28, role="backend")


# Function 3: menerima *args dan **kwargs, return tuple dan dict
def mix_args_kwargs(*args, **kwargs):
    return args, kwargs

t, k = mix_args_kwargs(1, 2, 3, name="mix_args_kwargs", age=28)
print(f"number: {t}")  # (1, 2, 3)
print(k)  # {'name': 'Acep', 'age': 28}


# Function 4: menampilkan dict langsung
def profile_print(**data):
    print(data)

profile_print(name="Acep", age=28, role="backend")


# Function 5: menampilkan args dan kwargs secara terpisah
def mix_params_display(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

mix_params_display("Acep", 28, city="Jakarta", role="Backend")
