while True:
    print("\n---- Student Record ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Add Student
    if choice == "1":
        name = input("Enter student name: ")

        with open("students.txt", "a") as f:
            f.write(name + "\n")

        print("Student Added Successfully!")

    # Option 2: View Students
    elif choice == "2":
        try:
            with open("students.txt", "r") as f:
                data = f.read()

                if data == "":
                    print("No students found.")
                else:
                    print("\n--- Student List ---")
                    print(data)

        except FileNotFoundError:
            print("No students found yet!")

    # Option 3: Exit
    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid ! Please try again.")