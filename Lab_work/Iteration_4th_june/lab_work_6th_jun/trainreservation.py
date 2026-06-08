# Train Reservation Waiting List

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

# Display waiting-list passengers
print("Waiting List Passengers:")
for name, status in passengers:
    if status == "Waiting":
        print(name)

# Count passengers and create separate lists
for name, status in passengers:
    if status == "Confirmed":
        confirmed_count += 1
        confirmed_list.append(name)
    else:
        waiting_count += 1
        waiting_list.append(name)

print("Confirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

# Find whether a specific passenger has a confirmed ticket
search_name = "Priya"

found = False
for name, status in passengers:
    if name == search_name and status == "Confirmed":
        found = True
        break

if found:
    print(search_name, "has a Confirmed ticket.")
else:
    print(search_name, "does not have a Confirmed ticket.")

# Separate lists
print("Confirmed List:", confirmed_list)
print("Waiting List:", waiting_list)