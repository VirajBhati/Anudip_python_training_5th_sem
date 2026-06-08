# Employee Performance Dashboard

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# 2. Count employees needing improvement
improvement_count = 0
for score in performance.values():
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement:", improvement_count)

# 3. Find the top performer
top_emp = ""
top_score = 0

for emp, score in performance.items():
    if score > top_score:
        top_score = score
        top_emp = emp

print("\nTop Performer:", top_emp, "(", top_score, ")", sep="")

# 4. Calculate average performance score
total = 0
for score in performance.values():
    total += score

average = total / len(performance)

print("\nAverage Score:", average)

# 5. Create separate lists
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)