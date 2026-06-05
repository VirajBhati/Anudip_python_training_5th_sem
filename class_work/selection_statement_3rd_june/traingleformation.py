#program of converting the time in minutes to corresponding time in hour, minute and second 
print("---------Time Converter-----------")
#input of time in seconds
second = int(input("enter time in second: "))
#check second in negative 
if(second <0):
    exit("time cannot be negative.........exited")
#----------------------------------------------------------------
print("-------------------------------------------------")
hours = 0
minutes = 0
#converting number of second into hours 
if(second >= 3600):
    hours = second // 3600
    second = second % 3600
#----------------------------------------------------------------
#converting into minutes
if(second >= 60):
    minutes = second // 60
    second = second % 60
#----------------------------------------------------------------
#converting into seconds
if(second >= 0):
    print("Time in hour : ", hours)
    print("Time in minute : ", minutes)
    print("Time in second : ", second)
    print("Time =", hours,":",minutes,":",second)