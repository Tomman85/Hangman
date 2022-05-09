import random
import time
import os

# # Initial Steps to invite in the game:
# print("\nWelcome to Hangman game by DataFlair\n")
# name = input("Enter your name: ")
# print("Hello " + name + "! Best of Luck!")
# time.sleep(2)
# print("The game is about to start!\n Let's play Hangman!")
# time.sleep(3)


# The parameters we require to execute the game:

words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage"
    , "plants"]
word = random.choice(words_to_guess)
length = len(word)
count = 0
display_list = list('_' * length)
already_guessed = []
play_game = ""
life = 5

print(word)


def hangman():
    global display, life

    while life > 0:
        player_input = input(f"This is the Hangman Word: {''.join(display_list)}")
        strip_length = len(player_input.strip())

        if strip_length == 1 and f"{player_input}" in word:
            for i in range(len(display_list)):
                if player_input == word[i]:
                    display_list[i] = f"{player_input}"
            if display_list == list(word):
                print("nice")
                break
        elif strip_length == 1 and player_input not in word:

            print("Nie poprawna litera")
            life -= 1
            if life == 4:
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif life == 3:

                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif life == 2:
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif life == 1:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     0\n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif life == 0:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")

        else:
            print("Wprowadz poprawną litere ")

        print("")


hangman()
