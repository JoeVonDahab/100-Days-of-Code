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

# Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice == 0:
    if computer_choice == 0:
        print('You chose rock and computer chose rock too. It is a draw.\n')
        print(rock, rock)
    elif computer_choice == 1:
        print('You chose rock, and computer chose paper. You lose.\n')
        print(rock, paper)
    elif computer_choice == 2:
        print('You chose rock, and computer chose scissors. You win.\n')
        print(rock, scissors)
elif user_choice == 1:
    if computer_choice == 0:
        print('You chose paper, and computer chose rock. You win.\n')
        print(paper, rock)
    elif computer_choice == 1:
        print('You chose paper and computer chose paper too. It is a draw.\n')
        print(paper, paper)
    elif computer_choice == 2:
        print('You chose paper, and computer chose scissors. You lose.\n')
        print(paper, scissors)
elif user_choice == 2:
    if computer_choice == 0:
        print('You chose scissors, and computer chose rock. You lose.\n')
        print(scissors, rock)
    elif computer_choice == 1:
        print('You chose scissors, and computer chose paper. You win.\n')
        print(scissors, paper)
    elif computer_choice == 2:
        print('You chose scissors and computer chose scissors too. It is a draw.\n')
        print(scissors, scissors)
else:
    print("Invalid choice. Please choose 0 for Rock, 1 for Paper or 2 for Scissors.")

input("Press Enter to continue...")
