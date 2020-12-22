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

selected_choice = [rock, paper, scissors]
user_choice = 3
while user_choice not in [0,1,2]:
    user_choice = int(input("Please type from the given choice? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(selected_choice[user_choice])


robot_choice = random.randint(0, 2)
print("Computer chose:")
print(selected_choice[robot_choice])


if user_choice == 0 and robot_choice == 2:
    print("You win!")
elif robot_choice == 0 and user_choice == 2:
    print("You lose")
elif robot_choice > user_choice:
    print("You lose")
elif user_choice > robot_choice:
    print("You win!")
elif robot_choice == user_choice:
    print("It's a draw")