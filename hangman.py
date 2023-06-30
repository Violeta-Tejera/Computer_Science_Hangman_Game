from random import choice
import csv

# Possible words to pick from. Might update this someday into a dictionary that teaches the word after it is discovered (Maybe with categories too :D)
words = {}
with open("words.csv",'r') as file:
    reader = csv.reader(file, delimiter="#")
    for row in reader:
        key = row[0]
        value = row[1]
        words[key] = value        

correct_letters = [] # Correct letters the player has guessed
incorrect_letters = [] # Incorrect letters the player has tried
unique_letters = [] # Letters present in the word
lives = 6 # Lives start at 6. Each time there's an incorrect letter chosen, lives discounts by one unit.
right_guesses = 0 # Counter
end_game = False

# This function picks a random word from the possible ones and appends the letters present in the word to the list unique_letters
def choose_word():
    word = choice(list(words.keys()))
    for i in range(0, len(word)):
        if word[i] not in unique_letters:
            unique_letters.append(word[i])

    return word, unique_letters

# This function asks the player for a letter. It doesn't matter if the letter is lowercase or uppercase. Any invalid character is dropped
# and the function handles reprompting the player for a letter until a valid character is inputted.
def request_letter():
    chosen_letter = ''
    letter_is_valid = False

    while not letter_is_valid:
        chosen_letter = input("Pick a letter: ")
        if ord(chosen_letter.upper()) >= 65 and ord(chosen_letter.upper()) <= 90:
            letter_is_valid = True
        else:
            print(chosen_letter + " is not a valid letter")
    
    return chosen_letter.upper()

# This function checks whether or not the letter inputted by the player is present in the word and acts
# accordingly: If the letter is not present, the lives are reduced by one. If it's present, it adds it to
# the word. Afterwards, if lives reach 0 or the word is completed, the game ends.
def check_letter(letter, word, lives, right_guesses):
    end_game = False
    
    if letter in word:
        correct_letters.append(letter)
        right_guesses += 1
    else:
        incorrect_letters.append(letter)
        lives -= 1

    if lives == 0:
        end_game = lose()
    elif right_guesses == unique_letters_quantity:
        end_game = win(word)
    
    return lives, end_game, right_guesses

# Prints some game over messages and ends the game.
def lose():
    print("You have run out of lives")
    print("Hidden word was " +word)
    end_game = True

# Prints some game over messages and ends the game.
def win(word):
    display_progress()
    print("You have discovered the word")
    end_game = True

# Prints the word with underscores in not discovered letters
def display_progress():
    progress = []

    for letter in word:
        if letter in correct_letters:
            progress.append(letter)
        else:
            progress.append('_')

    print(" ".join(progress))

word, unique_letters = choose_word()
unique_letters_quantity = len(unique_letters)

# Main program
while end_game == False:
    print("\n" + "#" * 30 + "\n")
    display_progress()
    print("\n")
    print("Incorrect letters: " + ', '.join(incorrect_letters))
    print(f'Lives: {lives}')
    print("\n" + "#" * 30 + "\n") 
    
    this_letter = request_letter()
    lives, end_game, right_guesses = check_letter(this_letter, word, lives, right_guesses)



