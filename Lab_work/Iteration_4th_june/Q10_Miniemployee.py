name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

da = 0.20 * basic      # Dearness Allowance (20%)
hra = 0.10 * basic     # House Rent Allowance (10%)

gross_salary = basic + da + hra

print("\nEmployee Name:", name)
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("Gross Salary:", gross_salary)
