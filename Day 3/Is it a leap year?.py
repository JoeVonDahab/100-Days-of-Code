# Which year do you want to check?
year = int(input("Please enter the year: "))
is_it_a_leap = False

# Check if the year is a leap year
if (year % 400) == 0:
    is_it_a_leap = True
elif (year % 100) == 0:
    is_it_a_leap = False
elif (year % 4) == 0:
    is_it_a_leap = True

# Output the result
if is_it_a_leap:
    print('It is a Leap Year!')
else:
    print('It is not a Leap Year :(')

# Wait for the user to press Enter before exiting
input("Press Enter to exit the program...")
