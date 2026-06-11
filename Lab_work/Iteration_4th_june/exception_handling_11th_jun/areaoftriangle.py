try:
    # Input sides of triangle
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    # Check if sides are positive
    if a <= 0 or b <= 0 or c <= 0:
     raise ValueError("Triangle sides must be greater than zero.")
    # Heron's Formula
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print("Area of the triangle =", round(area, 2))

except ValueError as e:
    print("Error:", e)

except:
    print("Error: Please enter numeric values only.")

finally:
    print("Triangle area calculation process completed.") 