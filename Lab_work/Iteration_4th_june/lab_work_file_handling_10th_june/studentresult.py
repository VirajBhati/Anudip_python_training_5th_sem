# Function to read student records from file
def read_results():
    students = []

    file = open("results.txt", "r")

    for line in file:
        data = line.strip().split(",")
        students.append([data[0], data[1], int(data[2])])

    file.close()
    return students


# Display all records
def display_records():
    students = read_results()

    print("\nStudent ID\tName\tMarks")
    print("-" * 35)

    for student in students:
        print(student[0], "\t", student[1], "\t", student[2])


# Search student by ID
def search_student(student_id):
    students = read_results()

    for student in students:
        if student[0] == student_id:
            print("\nStudent Found")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Marks:", student[2])
            return

    print("Student not found.")


# Find topper and lowest scorer
def topper_lowest():
    students = read_results()

    topper = students[0]
    lowest = students[0]

    for student in students:
        if student[2] > topper[2]:
            topper = student

        if student[2] < lowest[2]:
            lowest = student

    print("\nTopper:")
    print(topper[0], topper[1], topper[2])

    print("\nLowest Scorer:")
    print(lowest[0], lowest[1], lowest[2])


# Calculate class average
def class_average():
    students = read_results()

    total = 0

    for student in students:
        total += student[2]

    average = total / len(students)

    print("\nClass Average =", average)


# Count pass and fail students
def pass_fail_count():
    students = read_results()

    passed = 0
    failed = 0

    for student in students:
        if student[2] >= 40:
            passed += 1
        else:
            failed += 1

    print("\nPassed Students =", passed)
    print("Failed Students =", failed)


# Generate grades and write to file
def generate_grades():
    students = read_results()

    file = open("grades.txt", "w")

    for student in students:
        marks = student[2]

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"

        file.write(f"{student[0]},{student[1]},{marks},{grade}\n")

    file.close()

    print("Grade report generated successfully in grades.txt")


# Main Menu
while True:
    print("\n===== STUDENT RESULT PROCESSING SYSTEM =====")
    print("1. Display All Records")
    print("2. Search Student")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades Report")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        sid = input("Enter Student ID: ")
        search_student(sid)

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail_count()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")