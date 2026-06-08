# Cricket Tournament Statistics

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player, run in runs.items():
    if run > 500:
        print(player)

# 2. Find the Orange Cap winner
orange_cap = ""
max_runs = 0

for player, run in runs.items():
    if run > max_runs:
        max_runs = run
        orange_cap = player

print("\nOrange Cap Winner:", orange_cap, "(", max_runs, ")", sep="")

# 3. Find the lowest scorer
lowest_player = ""
lowest_runs = float('inf')

for player, run in runs.items():
    if run < lowest_runs:
        lowest_runs = run
        lowest_player = player

print("\nLowest Scorer:", lowest_player, "(", lowest_runs, ")", sep="")

# 4. Calculate total runs scored
total_runs = 0

for run in runs.values():
    total_runs += run

print("\nTotal Tournament Runs:", total_runs)

# 5. Create a list of players scoring below 400
below_400 = []

for player, run in runs.items():
    if run < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# 6. Count players scoring between 400 and 600 runs
count = 0

for run in runs.values():
    if 400 <= run <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)