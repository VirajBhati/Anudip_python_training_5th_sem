# Cricket Scoreboard Analysis

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Display players who scored 50 or more runs
print("Players scoring 50 or more runs:")
for player, score in scores.items():
    if score >= 50:
        print(player, ":", score)

# Count the number of centuries
centuries = 0
for score in scores.values():
    if score >= 100:
        centuries += 1

print("\nNumber of Centuries:", centuries)

# Find the player with the highest score
highest_player = ""
highest_score = 0

for player, score in scores.items():
    if score > highest_score:
        highest_score = score
        highest_player = player

print("\nHighest Scorer:", highest_player, "-", highest_score)

# Create a list of players scoring below 30 runs
below_30 = []

for player, score in scores.items():
    if score < 30:
        below_30.append(player)

print("\nPlayers scoring below 30 runs:")
print(below_30)

# Count players scoring between 50 and 99
count_50_99 = 0

for score in scores.values():
    if 50 <= score <= 99:
        count_50_99 += 1

print("\nPlayers scoring between 50 and 99:", count_50_99)