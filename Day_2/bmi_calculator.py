# mathematical operation in python
# pemdas left to right
# Parenthesis Exponent Multiplication(same level), Division(same level), addition(same level), substraction(same level)
# use python inbuilt <round> function to get rounded numbers
# replacing int in line 8 with round
# summary: <round> is used to get whole numbers / rounded numbers in py
height = float(input("Height: "))
weight = float(input("Weight: "))
bmi = weight / (height ** 2)
print(round(bmi))
