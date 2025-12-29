# Student Result Management System (Grades + Attendance)

students = {}

while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student")
    print("2. Enter Marks")
    print("3. Mark Attendance")
    print("4. View Full Result")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # 1. Add Student
    if choice == "1":
        student_id = input("Enter Student ID: ").strip()

        if student_id in students:
            print("Student already exists.")
        else:
            name = input("Enter Student Name: ").strip()
            students[student_id] = {
                "name": name,
                "marks": {},
                "total": 0,
                "percentage": 0,
                "grade": "",
                "present": 0,
                "attendance_total": 0
            }
            print("Student added successfully.")

    # 2. Enter Marks
    elif choice == "2":
        student_id = input("Enter Student ID: ").strip()

        if student_id not in students:
            print("Student not found.")
        else:
            try:
                maths = int(input("Enter Maths marks: "))
                physics = int(input("Enter Physics marks: "))
                cs = int(input("Enter CS marks: "))

                total = maths + physics + cs
                percentage = total / 3

                if percentage >= 85:
                    grade = "A"
                elif percentage >= 70:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C"
                else:
                    grade = "Fail"

                students[student_id]["marks"] = {
                    "Maths": maths,
                    "Physics": physics,
                    "CS": cs
                }
                students[student_id]["total"] = total
                students[student_id]["percentage"] = percentage
                students[student_id]["grade"] = grade

                print("Marks entered successfully.")

            except ValueError:
                print("Please enter valid numeric marks.")

    # 3. Mark Attendance
    elif choice == "3":
        student_id = input("Enter Student ID: ").strip()

        if student_id not in students:
            print("Student not found.")
        else:
            while True:
                status = input("Enter P for Present or A for Absent: ").strip().upper()

                if status in ["P", "A"]:
                    students[student_id]["attendance_total"] += 1
                    if status == "P":
                        students[student_id]["present"] += 1
                        print("Attendance marked Present.")
                    else:
                        print("Attendance marked Absent.")
                    break
                else:
                    print("Invalid input. Enter P or A only.")

    # 4. View Full Result
    elif choice == "4":
        student_id = input("Enter Student ID: ").strip()

        if student_id not in students:
            print("Student not found.")
        else:
            data = students[student_id]
            attendance_percent = (
                (data["present"] / data["attendance_total"]) * 100
                if data["attendance_total"] > 0 else 0
            )

            status = "PASS"
            if data["grade"] == "Fail" or attendance_percent < 75:
                status = "DETENTION / FAIL"

            print("\n--- Student Result ---")
            print(f"Name: {data['name']}")

            if data["marks"]:
                print(f"Marks: {data['marks']}")
                print(f"Percentage: {data['percentage']:.2f}%")
                print(f"Grade: {data['grade']}")
            else:
                print("Marks not entered.")

            print(f"Attendance: {data['present']}/{data['attendance_total']} ({attendance_percent:.2f}%)")
            print(f"Final Status: {status}")

    # 5. Exit
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 to 5.")
