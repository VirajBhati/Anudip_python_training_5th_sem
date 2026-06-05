num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")
