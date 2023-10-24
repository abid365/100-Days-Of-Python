# columns a,b,c; row 1,2,3, A3 will define the position of 1st column and 3rd row
# coding: utf-8

line1 = ["█", "█", "█"]
line2 = ["█", "█", "█"]
line3 = ["█", "█", "█"]

map = [line1, line2, line3]
print('Hiding your treasure! X marks the spot')
position = input()

# gets the letter from input , ex: letter variable will return A for the value of A3
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

print(f"{line1}\n{line2}\n{line3}")
