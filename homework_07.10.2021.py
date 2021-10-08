import random
playerOption = 0
wordList = ["apple"]

while playerOption != 3:
    print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program")
    playerOption = input("Enter number: ")
    randomWord = random.choice(wordList)
    linesForPrinting = ["-"] * len(randomWord)

    if int(playerOption) == 1:
        guessingWord = randomWord
        guessedLetterList = []
        cycleCounter = 0

        while cycleCounter != 5:

            listOFPictures = ["+---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n      |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n  |   |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|   |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n /    |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n /\   |\n=========",
                              ]
            print(listOFPictures[cycleCounter])
            print("Guessed letters: {}".format(guessedLetterList))
            print(*linesForPrinting)

            playerLetterInput = input("Enter letter: ")
            guessedLetterList.append(playerLetterInput)
            x = 0

            for slaveVariable in guessingWord:

                if slaveVariable == playerLetterInput:
                    linesForPrinting[x] = slaveVariable
                    x += 1

                elif slaveVariable != playerLetterInput:
                    x += 1

                elif x == len(linesForPrinting) - 1:
                    cycleCounter += 1
                    break

    elif int(playerOption) == 2:
        playerAddWord = input("Enter new word: ")
        wordList.append(playerAddWord)
        print("Added "+playerAddWord)

    elif int(playerOption) == 3:
        break

    else:
        print("Wrong input!")
