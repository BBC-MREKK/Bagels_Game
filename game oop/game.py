import random
from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, numdigits, maxguess):
        self.NUMDIGITS = numdigits
        self.MAXGUESS = maxguess

    @abstractmethod
    def getSecretNum(self):
        pass

    @abstractmethod
    def getClues(self, guess, secretNum):
        pass

    def isOnlyDigits(self, num):
        if num == '':
            return False
        for i in num:
            if i not in '0123456789':
                return False
        return True

    def playAgain(self):
        print('Хотите попробовать еще раз? ("Да" или "Нет")')
        return input().lower().startswith('y')

    def playGame(self):
        while True:
            secretNum = self.getSecretNum()
            print('\nИтак, я задумал число. У тебя %s попыток, чтобы угадать его.' % (self.MAXGUESS))

            numGuesses = 1
            while numGuesses <= self.MAXGUESS:
                guess = ''
                while len(guess) != self.NUMDIGITS or not self.isOnlyDigits(guess):
                    print('\nПопытка #%s: ' % (numGuesses))
                    guess = input()

                clue = self.getClues(guess, secretNum)
                print(clue)
                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses > self.MAXGUESS:
                    print('\nТебе не удалось отгадать мое число. Правильный ответ - %s.' % (secretNum))

            if not self.playAgain():
                break

class BagelsGame(Game):
    def getSecretNum(self):
        numbers = list(range(10))
        random.shuffle(numbers)
        secretNum = ''
        for i in range(self.NUMDIGITS):
            secretNum += str(numbers[i])
        return secretNum

    def getClues(self, guess, secretNum):
        if guess == secretNum:
            return '\nПревосходно! Вы угадали задуманное число!'

        clue = []

        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clue.append('Fermi')
            elif guess[i] in secretNum:
                clue.append('Pico')
        if len(clue) == 0:
            return 'Bagels'

        clue.sort()
        return ' '.join(clue)

if __name__ == "__main__":
    NUMDIGITS = 2
    MAXGUESS = 10

    print('Я загадаю %s-значное число. Попытайся угадать его.' % (NUMDIGITS))
    print('Ты будешь получать некоторые подсказки:')
    print('Подсказка:    Значение:')
    print('  Pico        Одна из цифр угадана верно, но стоит не на своей позиции.')
    print('  Fermi       Одна из цифр угадана верно и стоит на своей позиции.')
    print('  Bagels      Все цифры угаданы не верно.')

    game = BagelsGame(NUMDIGITS, MAXGUESS)
    game.playGame()