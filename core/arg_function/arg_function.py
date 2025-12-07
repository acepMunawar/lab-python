# =============================== *args func
# ======== menerima parameter bebas (dictionary)

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))   # 10

def mix(*biodata):
    return biodata

print(mix("acepmunawar",31))

def list_mix_void(*biodata):
    return list(biodata)

print(list_mix_void("acep", 31))

def print_biodata(*biodata):
    for data in biodata:
        print(data)

print_biodata("acepmunawar", 31, "Jakarta")

def print_biodata_order(*biodata):
    name, age, city = biodata
    print(name)
    print(city)
    print(age)

print_biodata_order("acepmunawar", 31, "Jakarta")


def mix_arg_params(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

mix_arg_params("Acep", 28, city="Jakarta", role="Backend")
