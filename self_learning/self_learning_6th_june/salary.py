# Employee Salary Processing

salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Display employees earning above ₹60,000
print("Employees earning above ₹60,000:")
for emp_id, sal in salary.items():
    if sal > 60000:
        print(emp_id, ":", sal)

# Count employees earning below ₹40,000
count = 0
for sal in salary.values():
    if sal < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)

# Find the highest-paid employee
highest_emp = ""
highest_salary = 0

for emp_id, sal in salary.items():
    if sal > highest_salary:
        highest_salary = sal
        highest_emp = emp_id

print("\nHighest-Paid Employee:", highest_emp, "-", highest_salary)

# Create a list of employees eligible for bonus
bonus_list = []

for emp_id, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp_id)

print("\nEmployees Eligible for Bonus:")
print(bonus_list)

# Calculate average salary
total_salary = 0

for sal in salary.values():
    total_salary += sal

average_salary = total_salary / len(salary)

print("\nAverage Salary:", average_salary)