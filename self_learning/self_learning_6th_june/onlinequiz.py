# Online Quiz Performance

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Display students scoring 15 or above
print("Students scoring 15 or above:")
for student, score in quiz_scores.items():
    if score >= 15:
        print(student, ":", score)

# Count students scoring below 10
count_below_10 = 0
for score in quiz_scores.values():
    if score < 10:
        count_below_10 += 1

print("\nStudents scoring below 10:", count_below_10)

# Find the top performer
top_student = ""
top_score = 0

for student, score in quiz_scores.items():
    if score > top_score:
        top_score = score
        top_student = student

print("\nTop Performer:", top_student, "-", top_score)

# Create a list of students who passed
passed_students = []

for student, score in quiz_scores.items():
    if score >= 10:
        passed_students.append(student)

print("\nPassed Students:")
print(passed_students)

# Calculate class average
total = 0
for score in quiz_scores.values():
    total += score

average = total / len(quiz_scores)

print("\nClass Average:", average)