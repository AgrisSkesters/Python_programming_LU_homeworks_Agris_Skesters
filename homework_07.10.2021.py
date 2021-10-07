playerOption = 0
wordList = []

while playerOption != 3:
    print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program")
    playerOption = int(input("Enter number: "))

    if playerOption == 1:
        cycleCounter = 3

        while cycleCounter != 5:

            print(listOFPictures[cycleCounter])
            playerLetterInput = input("Enter letter: ")

    elif playerOption == 2:
        playerAddWord = input("Enter new word: ")
        wordList.append(playerAddWord)
        print("Added "+playerAddWord)

    elif playerOption == 3:
        break

    else:
        print("Wrong input!")

listOFPictures = ["+---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n      |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n  |   |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|   |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n /    |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n /\   |\n=========",
                              ]

