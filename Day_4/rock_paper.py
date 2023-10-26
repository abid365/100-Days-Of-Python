import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors \n"))
computer_choice = random.randint(0,2)
print(f"computer choose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice == 1 and user_choice == 0:
    print("You lose")
elif computer_choice == 2 and user_choice == 1:
    print("")
elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("You typed a wrong number")


#todo: finish the task and do a case study