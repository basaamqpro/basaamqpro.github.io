def heart_calculation():
	time = int(input("Enter your time: "))
	print(time)
	return time
20
new_time = heart_calculation()

if(new_time > 10):
 print("New time is:", new_time)
else:
 print("Time is less than 10")