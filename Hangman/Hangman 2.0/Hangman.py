import random
from Hangman_wordlist import word_list
from Hangman_art import stages, logo
import os


print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = len(stages) - 1

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guess_list = [] 
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess in guess_list:
        print(f"You've already guessed {guess} and it is not in the word.")
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        guess_list.append(guess)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose and the word is", chosen_word)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])