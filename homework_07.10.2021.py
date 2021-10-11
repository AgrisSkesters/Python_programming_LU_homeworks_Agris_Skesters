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

        while cycleCounter != 6:

            listOFPictures = ["+---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n      |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n  |   |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|   |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n      |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n /    |\n      |\n=========",
                              "+---+\n  |   |\n  o   |\n /|\  |\n /\   |\n      |\n=========",
                              ]
            print(listOFPictures[cycleCounter])
            print("Guessed letters: {}".format(guessedLetterList))
            print(*linesForPrinting)

            playerLetterInput = input("Enter letter: ")
            guessedLetterList.append(playerLetterInput)
            wordSymbolCounter = 0
            guessedSymbolCounter = 0

            for slaveVariable in guessingWord:

                if slaveVariable == playerLetterInput:
                    linesForPrinting[wordSymbolCounter] = slaveVariable
                    guessedSymbolCounter += 1
                    wordSymbolCounter += 1

                elif wordSymbolCounter == len(linesForPrinting) - 1 and guessedSymbolCounter == 0:
                    cycleCounter += 1
                    break

                else:
                    wordSymbolCounter += 1

            str1 = "".join(str(e) for e in linesForPrinting)
            if str1 == guessingWord:
                print(guessingWord)
                print("You won!")
                break
        else:
            print("You lost!")

    elif int(playerOption) == 2:
        playerAddWord = input("Enter new word: ")
        wordList.append(playerAddWord)
        print("Added "+playerAddWord)

    elif int(playerOption) == 3:
        break

    else:
        print("Wrong input!")
