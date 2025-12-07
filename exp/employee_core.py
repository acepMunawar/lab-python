running = True

data_mahasiswa = []

while running:
    print("================================== Students ==================================")
    print("1. Add Students")
    print("2. Display Students")
    print("3. Exit")
    
    input_action = input("input menu: ")

    match input_action:
        case "1":
            student_name = input("Add Student")
            data_mahasiswa.append(student_name)
            print(f"Student '{student_name}' added successfully")
        case "2":
            if not data_mahasiswa:
                print("No students available.")
                continue

            print("\n======= Display Students =======")
            for idx, item in enumerate(data_mahasiswa, start=1):
                print(f"{idx}. {item}")

            print("\nOptions:")
            print("1. Update Student")
            print("2. Remove Student")
            print("3. Back to Main Menu")

            sub_action = input("Input option: ")
        
            if sub_action == "1":
                student_no = int(input("Enter student number to update: "))
                if 1 <= student_no <= len(data_mahasiswa):
                    print(f"ping kodisi {student_no} and {len(data_mahasiswa)}")
                    new_name = input("Enter new name: ")
                    old_name = data_mahasiswa[student_no - 1]
                    data_mahasiswa[student_no - 1] = new_name
                    print(f"Student '{old_name}' updated to '{new_name}'.")
                else:
                    print("Invalid number!")                
            elif sub_action == "2":
                student_no = int(input("Enter student number to remove: "))
                if 1 <= student_no <= len(data_mahasiswa):
                    removed = data_mahasiswa.pop(student_no - 1)
                    print(f"Student '{removed}' removed successfully.")
                else:
                    print("Invalid student number.")
            elif sub_action == "3":
                continue
            else:
                print("Invalid option.")
        case "3":
            running = False     
            print("Exiting program...")
