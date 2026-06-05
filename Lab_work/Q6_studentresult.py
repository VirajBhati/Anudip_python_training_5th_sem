name = input("Enter Student Name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

if percentage >= 60:
    grade = "First Division"
elif percentage >= 45:
    grade = "Second Division"
elif percentage >= 33:
    grade = "Third Division"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", grade)
