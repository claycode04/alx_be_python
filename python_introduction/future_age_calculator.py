try:
	input_age = int(input("Enter your current age: "))
	print("In 2050, you will be", input_age + 27, "years old.")
except ValueError:
	print("Please enter a valid integer for your age.")