student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#code below this line
total_height = 0
for height in student_heights:
    total_height += height
    print(f"total heights = {total_height} ")

total_students = 0
for students in student_heights:
    total_students += 1
    print(f"Number of students {total_students}")

avg_height = total_height / total_students
print(f"Average Height: {avg_height}")

