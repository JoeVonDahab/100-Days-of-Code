# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_heights = 0
total_students = 0
for height in student_heights:
  total_heights += height
  total_students += 1
average = round(total_heights/total_students)
# Write your code below this row 👇
print (f'''total height = {total_heights}
number of students = {total_students}
average height = {average}''')
input('press smth')
