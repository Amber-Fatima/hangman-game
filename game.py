import random
words = ['friends', 'cellphone', 'suitcase', 'sneakers']
# selects a random word to guess
sel_word = random.choice(words)
print(f'ssh you need to guess this word :{sel_word}')
display = ["_"]*len(sel_word)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# print(display)
# no of chance left to win the game
life = 7
while life > 0 and display.count("_") > 0:
    user = input()

    for i in range(len(sel_word)):
        if user == sel_word[i]:
            display[i] = user
# if the user guesses same letter(user) again or a wrong letter,he loses a point
# this is done by replacing the guessed letter by "-"

    if user in sel_word:
        sel_word = sel_word.replace(user, "-")

    else:

        life -= 1
        print(stages[life])

    print(display)
if life == 0 or display.count("_") > 0:
    print("please try again")
else:
    print("Congratulations,you won!")
