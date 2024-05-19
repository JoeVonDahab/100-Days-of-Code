target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
for number in range(0, target +1 ):
  if target < 1000:
    if number % 2 == 0:
      sum += number
  else:
    print ('Please enter number less than 1000')
print(sum)
    
