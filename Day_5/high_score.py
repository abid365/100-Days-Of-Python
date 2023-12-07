#input a list of student score
student_scores= input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
#your code below this line

highest_scores = 0
for score in student_scores:
    if(score > highest_scores):
        highest_scores = score
print(f"highest score is {highest_scores}")