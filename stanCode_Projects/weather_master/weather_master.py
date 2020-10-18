"""
File: weather_master.py
Name: Tao-Ke Chorng
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():
	"""
	The program will deal with the weather data that the user entered.
	"""
	print("\"Weather Master 4.0\"!")
	cold = 0
	# Ask user enter the 1st temperature, then evaluate the temperature and process it with initial parameters.
	tem = int(input("Next Temperature: (or -100 to quit)? "))
	counter = 1
	total = tem
	cold = 0
	if tem < 16:
		cold += 1
	# Tell user they do not enter a temperature
	if tem == -100:
		print("No temperature were entered.")
	else:
		# Set the initial highest and lowest temperature.
		high = tem
		low = tem
		# Using while loop to ask user to enter temperatures until -100 were entered
		while True:
			tem = int(input("Next Temperature: (or -100 to quit)? "))
			"""
			check the value of the new entered temperature with the following if statement, then set the new highest,
			lowest, cold days or do nothing.
			"""
			# Check the new entered temperature with the following if statement, then set the value to the variable when
			# meet the if condition.
			if tem == -100:
				break
			if tem > high:
				high = tem
				total += tem
				counter += 1
			if high > tem > low:
				total += tem
				counter += 1
			if low > tem:
				low = tem
				total += tem
				counter += 1
			if tem < 16:
				cold += 1
		print("Highest Temperature: " + str(high))
		print("Lowest Temperature: " + str(low))
		print("Average: "+ str(total / counter))
		print(str(cold)+" cold day(s)")
###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
