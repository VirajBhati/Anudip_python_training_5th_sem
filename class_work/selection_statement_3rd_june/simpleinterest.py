#$program to calculate simple interest
#---------------------------------------------------------------
print("------------------simple interest------------------")
#taking input from user
amt=int(input("enter the amount:"))
rate=int(input("enter rate of interst:"))
time=int(input("enter the time:"))
#---------------------------------------------------------------
#calculating simple interest
si=(amt * rate * time)/100
print("simple interest :",si)