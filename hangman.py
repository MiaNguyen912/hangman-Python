import random
import os
from word_list import word_list 
from hangman_art import stages, logo
#------------------

lives = 6
guessed_letter = [""]
print(logo)

#get random word from word_list
chosen_word = random.choice(word_list)  
#print(f'the solution is {chosen_word}.')
#--------------------

#Create blank
display = []
for letter in chosen_word:
  #display.append("_")
  display += "_"
print(f"{' '.join(display)}")
print(stages[lives])
#--------------------

#Ask the user to guess a letter, Make guess lowercase. Check that letter
while "_" in display:
  guess = ""
  while guess in guessed_letter:
    guess = input("Guess a letter: ").lower()
    if guess not in guessed_letter:
        guessed_letter += guess #add letter to the guessed_letter list
        break #stop asking user to guess
    else:
      print(f"You've guessed the letter {guess}")
  
  os.system('clear') #clear screen
  
  for index in range(len(chosen_word)):
    if chosen_word[index] == guess: #replace "_" with the correct letter
      display[index] = guess
  if guess not in display: #if no replacement was made
    lives -= 1
    print(f"\'{guess}\' is not in the word")
  print(stages[lives])
  print(f"{' '.join(display)}")
  if lives == 0:
    break #stop the while loop
#--------------------  

if "_" not in display:
  print("You Won!")
else:
  print("You Lose!")
