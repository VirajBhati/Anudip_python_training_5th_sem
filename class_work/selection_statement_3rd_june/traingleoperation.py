#program to calculate area an parameter of triangle 
#input of three sides
print("---------Triangle-----------")
side1 = int(input("enter first side (in cm) : "))
side2 = int(input("enter second side (in cm) : "))
side3 = int(input("enter third side (in cm) : "))
#--------------------------------------------
#to calculate perimeter
perimeter = side1 + side2 + side3
print("Perimeter of the triangle : ", perimeter, "cm")
#---------------------------------------------
#to calculate the area
s = perimeter/2                      #calculate of s
area = (s * (s-side1) * (s-side2) * (s-side3))**0.50
print("Area of the triangle : ",area,"sq.cm")

