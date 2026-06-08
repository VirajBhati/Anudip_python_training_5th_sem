# Smart Electricity Billing System

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house)

# 2. Find the highest-consuming house
highest_house = ""
highest_units = 0

for house, consumption in units.items():
    if consumption > highest_units:
        highest_units = consumption
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest_units, "units)", sep="")

# 3. Find the lowest-consuming house
lowest_house = ""
lowest_units = float('inf')

for house, consumption in units.items():
    if consumption < lowest_units:
        lowest_units = consumption
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest_units, "units)", sep="")

# 4. Calculate total units consumed
total_units = 0

for consumption in units.values():
    total_units += consumption

print("\nTotal Units Consumed:", total_units)

# 5. Create lists based on consumption
low_consumption = []
medium_consumption = []
high_consumption = []

for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
    elif consumption <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print("\nLow Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)

# 6. Count houses eligible for energy-saving campaign
campaign_count = 0

for consumption in units.values():
    if consumption > 300:
        campaign_count += 1

print("\nEligible for Energy-Saving Campaign:", campaign_count)