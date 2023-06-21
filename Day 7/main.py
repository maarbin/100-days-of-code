# from replit import clear
import random

import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art
print(hangman_art.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

duplicated = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clear()
    
    if guess in duplicated:
      print(f"You already typed {guess} letter. Try different letter.")
    else:
    #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
              duplicated += guess

      if guess not in chosen_word:
          print(f"Letter {guess} is not in word. You lose life.")
          lives -= 1
          duplicated += guess
          if lives == 0:
              end_of_game = True
              print(f"You lose - {chosen_word} was a word")
  
      print(f"{' '.join(display)}")
  
      if "_" not in display:
          end_of_game = True
          print("You win.")

    print(hangman_art.stages[lives])