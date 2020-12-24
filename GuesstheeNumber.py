from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)

guessing_number = randint(1,100)
print("Psst the guessing_number is ", guessing_number)

def check_result(guessed_number):
  if guessed_number == guessing_number:
    return True
  else:
    return False


def play_game(turns):
  print(f'YOU HAVE {turns} turns to guess.')
  while turns != 0:
    guessed_number = int(input("Guess the number: "))
    if check_result(guessed_number):
      return "You won"
    else:
      turns -= 1
      print(f'YOU HAVE now {turns} turns to guess.')
  
  return "You guessed wrong"

difficulty_level = input("Easy or difficult: ").lower()

if difficulty_level == 'easy':
  print(play_game(EASY_LEVEL_TURNS))
else:
  print(play_game(HARD_LEVEL_TURNS))