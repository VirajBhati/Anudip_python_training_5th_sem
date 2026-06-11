def display_records():
    file = open("employees.txt", "r")
    print("\nEmployee Records:")
    for line in file:
        print(line.strip())
    file.close()


def search_employee(emp_id):
    file = open("employees.txt", "r")

    found = False
    for line in file:
        data = line.strip().split(",")

        if data[0] == emp_id:
            print("\nEmployee Found:")
            print("ID:", data[0])
            print("Name:", data[1])
            print("Salary:", data[2])
            found = True
            break

    if not found:
        print("Employee not found!")

    file.close()


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")
        total += int(data[2])
        count += 1

    print("Average Salary =", total / count)

    file.close()


def highest_lowest_salary():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        data = line.strip().split(",")
        employees.append(data)

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:
        if int(emp[2]) > int(highest[2]):
            highest = emp

        if int(emp[2]) < int(lowest[2]):
            lowest = emp

    print("\nHighest Paid Employee:")
    print(highest[0], highest[1], highest[2])

    print("\nLowest Paid Employee:")
    print(lowest[0], lowest[1], lowest[2])

    file.close()


def above_50000():
    file = open("employees.txt", "r")

    print("\nEmployees earning above ₹50,000:")

    for line in file:
        data = line.strip().split(",")

        if int(data[2]) > 50000:
            print(data[0], data[1], data[2])

    file.close()


def add_employee():
    file = open("employees.txt", "a")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee added successfully!")


def salary_categories():
    file = open("employees.txt", "r")

    print("\nSalary Categories")

    for line in file:
        data = line.strip().split(",")
        salary = int(data[2])

        if salary >= 60000:
            category = "High"
        elif salary >= 40000:
            category = "Medium"
        else:
            category = "Low"

        print(data[0], data[1], "->", category)

    file.close()


# Main Menu
while True:
    print("\n===== Employee Payroll Management System =====")
    print("1. Display all employee records")
    print("2. Search employee by ID")
    print("3. Calculate average salary")
    print("4. Highest-paid and lowest-paid employee")
    print("5. Employees earning above ₹50,000")
    print("6. Add new employee")
    print("7. Salary categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        emp_id = input("Enter Employee ID: ")
        search_employee(emp_id)

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest_salary()

    elif choice == 5:
        above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_categories()

    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid Choice!")
