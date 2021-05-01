import random

def is_valid_letter(letter, input_letters):
    if len(letter) != 1:
        print("You should input a single letter")
        return False
    if not letter.isalpha() or not letter.islower():
        print("Please enter a lowercase English letter")
        return False
    if letter in input_letters:
        print("You've already guessed this letter")
        return False
    input_letters.add(letter)    
 
    return True

def game():
    answer = random.choice(('python', 'java', 'kotlin', 'javascript'))

    hint = "-" * len(answer)
    lives = 8 
    input_letters = set()
    
    print()

    while True:
        print(hint)
        letter = input("Input a letter: ")
        if not is_valid_letter(letter, input_letters):
            print()
            continue
        if letter not in answer:
            print("That letter doesn't appear in the word")
            lives -= 1
        else:
            hint_list = list(hint)
            for j in range(0, len(answer)):
                index = answer.find(letter, j)
                if index >= 0:
                    hint_list[index] = letter
            newhint = "".join(hint_list)
            if newhint != hint:
                hint = newhint
            else:
                print("No improvements")
                lives -= 1
        if hint == answer or lives == 0:
            break
        print()
    if lives == 0:
        print("You lost!")
    else:
        print("You guessed the word!")
        print("You survived!")
    print()

print("H A N G M A N")

menu = ""
while menu != "exit":
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
        game()