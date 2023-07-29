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

import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)

result = [["draw","lose","win"],["win","draw","lose"],["lose","win","draw"]]

if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
elif player_choice == 2:
  print(scissors)
else:
  print("You typed an invalid number! You lose.")

if comp_choice == 0:
  print("Computer chose:\n" + rock)
elif comp_choice == 1:
  print("Computer chose:\n" + paper)
else:
  print("Computer chose:\n" + scissors)

if player_choice == 0 or player_choice == 1 or player_choice == 2:
  print("You " + result[player_choice][comp_choice])

