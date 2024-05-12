# 1st input: enter height in meters e.g: 1.65
height = input("Please Enter your height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input('Please enter your weight in kilograms: ')
# 🚨 Don't change the code above 👆

# Convert input strings to float and calculate BMI
BMI = round(float(weight) / (float(height) ** 2), 2)

# Convert BMI to string for concatenation
print('Your BMI equals ' + str(BMI))
input("Press Enter to continue...")
