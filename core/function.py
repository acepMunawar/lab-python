
# =============================== Void function

def exp_function():
    print("this is function")

exp_function()

# == param function

def param_function(name, age):
    print(name, age)

param_function("acepmunawar", 31)
param_function("marlo", 31)
param_function("danis", 30)

# == Default param function

def greet(name="User"):
    print(f"Hello {name}")

greet()
greet("Acep")

# == Keyword arguments

def register(name, age, active=True):
    print(name, age, active)

register(age=28, name="Acep")


# =============================== Return function

def total(a, b):
    return a + b

hasil = total(5, 10)
print(hasil)

# =============================== Keyword Arguments Func
# ======== Sering di pakai untuk Clarity

def register(name, age, active=True):
    print(name, age, active)

register(age=28, name="Acep")


