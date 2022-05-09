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


def hangman():
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage"
        , "plants"]
    word = random.choice(words_to_guess)
    length = len(word)

    display_list = list('_' * length)

    life = 5
    should_continue = True
    print(word)

    while life > 0 and should_continue:
        life_chance = print(f"Twoja liczba szans: {life}\n")
        player_input = input(f"This is the Hangman Word: {''.join(display_list)} ").lower()
        strip_length = len(player_input.strip())
        if strip_length == 1 and f"{player_input}" in display_list:
            print("Litera została już podana")
            life -= 1
        elif strip_length == 1 and f"{player_input}" in word:
            for i in range(len(display_list)):
                if player_input == word[i]:
                    display_list[i] = f"{player_input}"

            if display_list == list(word):
                print(f"Gratulacje odgałeś/aś słowo: {''.join(display_list)} ")
                player_continue = input("Czy chcesz kontynuować rozgrywke, tak /t nie /n?").lower()
                if player_continue == 't':
                    word = random.choice(words_to_guess)

                    length = len(word)

                    display_list = list('_' * length)
                    life = 5
                else:
                    print("Dziękuję za gre ")
                    should_continue = False


        elif strip_length == 1 and player_input not in word:

            print("Nie poprawna litera")
            life -= 1
        else:
            print("Wprowadz poprawną litere ")
        if life == 4:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            life_chance
        if life == 3:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            life_chance

        if life == 2:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            life_chance

        if life == 1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     0\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            life_chance

        if life == 0:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            life_chance
            print(f"Niestety przegrałes słowo, które miałeś odgadnąć to {word}")
            player_continue = input("Czy chcesz kontynuować rozgrywke, tak /t nie /n?").lower()
            if player_continue == 't':
                word = random.choice(words_to_guess)

                length = len(word)

                display_list = list('_' * length)
                life = 5
            else:
                print("Dziękuję za gre ")
                break

    print("")


hangman()
