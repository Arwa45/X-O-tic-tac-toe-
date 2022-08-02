from math import inf as infinity
import random
HUMAN = 'O'
COMP = 'X'

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


printBoard(board)

print("Computer goes first! Good luck.")

print("Positions are as follow:")

print("1, 2, 3 ")

print("4, 5, 6 ")

print("7, 8, 9 ")

print("\n")



def spaceIsFree(position):
        return board[position] == ' '

def empty_cells(board):
    count = 0
    for key in board.keys():
        if (board[key] == ' '):
           count += 1
    return count

def checkWhichMarkWon(mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark))

def checkDraw():
    for cell in board:
        if (board[cell] == ' '):
            return False
    return True

def insertLetter(letter, position):

    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if (checkWhichMarkWon(letter)):
            if letter == 'X':
                print("COMPUTER wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

def playerMove():

    position = int(input("Enter the position for 'O':  "))
    insertLetter(HUMAN, position)
    return

def compMove():
    if empty_cells(board) == 9:
        insertLetter(COMP , random.randint(1 , 9))
        return
    bestScore = -infinity
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = COMP
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(COMP, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(COMP)):
        return 1
    elif (checkWhichMarkWon(HUMAN)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -infinity
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = COMP
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = infinity
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = HUMAN
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


while not (checkWhichMarkWon(COMP) or checkWhichMarkWon(HUMAN)):
    compMove()
    playerMove()