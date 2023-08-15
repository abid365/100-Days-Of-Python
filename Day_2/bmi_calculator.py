# mathematical operation in python
# pemdas left to right
# Parenthesis Exponent Multiplication(same level), Division(same level), addition(same level), substraction(same level)
# use python inbuilt <round> function to get rounded numbers
# replacing int in line 8 with round
# summary: <round> is used to get whole numbers / decimal places
# rounded(value, decimal places tobe executed)
# on line 12 the value will be printed rounded to two decimal places
height = float(input("Height: "))
weight = float(input("Weight: "))
bmi = weight / (height ** 2)
print(round(bmi))
print(round(8 / 3, 2))
