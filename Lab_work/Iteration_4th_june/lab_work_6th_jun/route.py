# Bus Route Monitoring

passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
busiest = passengers[0]
stop_no = 1

for i in range(len(passengers)):
    if passengers[i] > busiest:
        busiest = passengers[i]
        stop_no = i + 1

print("Busiest Stop:", stop_no, "with", busiest, "passengers")

# Display stops with fewer than 10 passengers
print("Stops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1, ":", passengers[i], "passengers")

# Calculate average passengers
total = 0
for p in passengers:
    total += p

average = total / len(passengers)
print("Average Passengers:", average)

# Determine whether any stop exceeded 25 passengers
exceeded = False
for p in passengers:
    if p > 25:
        exceeded = True
        break

if exceeded:
    print("Yes, at least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")