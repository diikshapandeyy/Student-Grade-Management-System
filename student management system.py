students = []


# Calculate grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Add student
def add_student():

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    if any(s["roll"] == roll for s in students):
        print("Roll number already exists!")
        return

    try:
        english = int(input("Enter English marks: "))
        maths = int(input("Enter Maths marks: "))
        science = int(input("Enter Science marks: "))

        marks = [english, maths, science]

        if any(mark < 0 or mark > 100 for mark in marks):
            print("Marks must be between 0 and 100.")
            return

        total = sum(marks)
        percentage = total / 3
        grade = calculate_grade(percentage)

        student = {
            "name": name,
            "roll": roll,
            "english": english,
            "maths": maths,
            "science": science,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)

        print("\nStudent added successfully!")

    except ValueError:
        print("Please enter valid numeric marks.")


# Display students
def display_students():

    if not students:
        print("\nNo student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for s in students:

        print("\nName:", s["name"])
        print("Roll Number:", s["roll"])
        print("English:", s["english"])
        print("Maths:", s["maths"])
        print("Science:", s["science"])
        print("Total:", s["total"], "/ 300")
        print("Percentage:", round(s["percentage"], 2), "%")
        print("Grade:", s["grade"])

        print("-----------------------------------")


# Search student
def search_student():

    roll = input("Enter roll number to search: ")

    for s in students:

        if s["roll"] == roll:

            print("\nStudent Found!")
            print("Name:", s["name"])
            print("Roll:", s["roll"])
            print("Percentage:", round(s["percentage"], 2))
            print("Grade:", s["grade"])

            return

    print("Student not found!")


# Delete student
def delete_student():

    roll = input("Enter roll number to delete: ")

    for s in students:

        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main menu
while True:

    print("\n====== STUDENT GRADE MANAGER ======")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice! Please try again.")