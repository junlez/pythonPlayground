# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


gameFinished = False
player = ("", "Player 1's move: ", "Player 2's move: ")
playerIndex = 1
boardRows, boardColumns = (3, 3)
sequenceNumber = 3
# board = [[2]*boardColumns]*boardRows #bad due to shadow lists
board = [[0 for i in range(boardColumns)] for j in range(boardRows)]

def ticTacToe_getInput():
    global boardRows, boardColumns
    global board

    playerInput = int(input(player[playerIndex]))
    # print(playerInput)
    index = 0
    # for i in reversed(range(boardRows)):
    for i in range(boardRows):
        for j in range(boardColumns):
            index = index + 1;
            # print(index)
            if(index == playerInput):
                board[i][j] = playerIndex
                # print("found: " + str(index))
                return

def ticTacToe_printBoard():
    global boardRows, boardColumns
    global board

    for i in range(boardRows):
        print(board[i])

def ticTacToe_analyzeBoard():
    global playerIndex
    global boardRows, boardColumns
    global board

    for i in range(boardRows):
        for j in range(boardColumns):
            xLimit = boardColumns - j
            yLimit = boardRows - i
            # print("xLimit: " + str(xLimit));
            # print("yLimit: " + str(yLimit));
            count = 0
            for k in range(xLimit):
                if (board[i][j + k] != playerIndex):
                    break
                count = count + 1
                # print("1, count: " + str(count));
                if(count == sequenceNumber):
                    return playerIndex
            count = 0
            for k in range(yLimit):
                if (board[i + k][j] != playerIndex):
                    break
                count = count + 1
                # print("2, count: " + str(count));
                if(count == sequenceNumber):
                    return playerIndex
            count = 0
            for k in range(min(xLimit, yLimit)):
                if (board[i + k][j + k] != playerIndex):
                    break
                count = count + 1
                # print("3, count: " + str(count));
                if (count == sequenceNumber):
                    return playerIndex
            yLimit = boardRows
            count = 0
            for k in range(min(xLimit, yLimit)):
                if (board[i - k][j + k] != playerIndex):
                    break
                count = count + 1
                # print("4, count: " + str(count));
                if (count == sequenceNumber):
                    return playerIndex
    return 0

def ticTacToe_switchPlayer():
    global playerIndex

    if(playerIndex == 1):
        playerIndex = 2
    else:
        playerIndex = 1

def ticTacToe():
    global gameFinished
    global playerIndex
    global boardRows, boardColumns
    global sequenceNumber

    print(boardRows)
    print(boardColumns)
    print(sequenceNumber)

    play = True

    while(play == True):
        ticTacToe_printBoard()
        while(gameFinished == False):
            ticTacToe_getInput()
            ticTacToe_printBoard()
            if(ticTacToe_analyzeBoard() == playerIndex):
                print("Player " + str(playerIndex) + " won!")
                gameFinished = True
                play = False
            ticTacToe_switchPlayer()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Junle')
    ticTacToe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
