# ================================== Condition If

print("Hello Python")

umur = 25

if umur >= 17:
    print("Sudah cukup umur")
else:
    print("Belum cukup umur")

umur = 12

if umur >= 17:
    print("sudah cukup umur")
elif umur >= 12:
    print("lumayan cukup umur")
else:
    print("tidak boleh daftar")

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True") 

a = 10
b = 33
c = 500

if a > b or c > a:
    print("Both conditions are True") 

# ================================== Condition chaining

print("Condition Chaining")     

data_mahasiswa = ["acep munawar","randi"]
student_no = 1

# kondisi di bawah setara dengan kondisi
# student_no >= 1 and student_no <= len(data_mahasiswa)

if 1 <= student_no <= len(data_mahasiswa):
    print(f"ping kodisi {student_no} and {len(data_mahasiswa)}")
else:
    print("Invalid number!")       

# ================================== Condition Switch Case/ Math Statement

day = 4

match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
         print("Looking forward to the Weekend")   