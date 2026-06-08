# Warehouse Product Inspection

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0

print("Failed Product IDs:")

for pid, status in products:
    if status == "Fail":
        print(pid)
        failed += 1

        # Stop checking if 3 failures are found
        if failed == 3:
            print("3 failures found. Stopping inspection.")
            break
    else:
        passed += 1

# Count passed and failed products
print("Passed Products:", passed)
print("Failed Products:", failed)

# Calculate pass percentage
total = passed + failed
pass_percentage = (passed / total) * 100

print("Pass Percentage:", pass_percentage, "%")