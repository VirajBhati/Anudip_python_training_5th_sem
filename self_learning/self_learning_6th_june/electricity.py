# Electricity Consumption Report

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Display houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, consumption in units.items():
    if consumption > 300:
        print(house, ":", consumption)

# Count houses consuming less than 200 units
count = 0
for consumption in units.values():
    if consumption < 200:
        count += 1

print("\nHouses consuming less than 200 units:", count)

# Find the house with the highest consumption
highest_house = ""
highest_consumption = 0

for house, consumption in units.items():
    if consumption > highest_consumption:
        highest_consumption = consumption
        highest_house = house

print("\nHouse with Highest Consumption:", highest_house, "-", highest_consumption)

# Create a list of houses eligible for energy-saving awareness campaign
campaign_list = []

for house, consumption in units.items():
    if consumption > 400:
        campaign_list.append(house)

print("\nHouses Eligible for Energy-Saving Awareness Campaign:")
print(campaign_list)

# Categorize houses
print("\nHouse Categories:")
for house, consumption in units.items():
    if consumption < 200:
        category = "Low"
    elif consumption <= 350:
        category = "Medium"
    else:
        category = "High"

    print(house, ":", category)