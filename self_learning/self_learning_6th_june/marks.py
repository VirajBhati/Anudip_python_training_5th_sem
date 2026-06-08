# Student Marks Analysis

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Students scoring 80 or above
print("Students scoring 80 or above:")
for name, score in marks.items():
    if score >= 80:
        print(name, ":", score)

# Count failed students
fail_count = 0
for score in marks.values():
    if score < 40:
        fail_count += 1

print("\nNumber of failed students:", fail_count)

# Find highest scorer
highest_name = ""
highest_marks = 0

for name, score in marks.items():
    if score > highest_marks:
        highest_marks = score
        highest_name = name

print("\nHighest Scorer:", highest_name, "-", highest_marks)

# Students scoring between 60 and 75
between_60_75 = []

for name, score in marks.items():
    if 60 <= score <= 75:
        between_60_75.append(name)

print("\nStudents scoring between 60 and 75:")
print(between_60_75)

# Assign Grades
print("\nGrades:")
for name, score in marks.items():
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, ":", grade)