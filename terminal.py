from tabulate import tabulate

board = ["*" for _ in range(9)]

count = 1

def displayBoard(board):
    
    groups, temp_board = [], []

    for _, __ in enumerate(board, 1):

        groups.append(__)

        if _ % 3 == 0:
            temp_board.append(groups)
            groups = []

    return tabulate(temp_board, tablefmt="grid")

def checkWin(board):

    wins = [
        (1,2,3), (4,5,6), (7,8,9), (1,5,9),
        (1,4,7), (2,5,8), (3,6,9), (3,5,7),
    ]

    for win in wins:

        if board[win[0] - 1] == board[win[1] - 1] == board[win[2] - 1]:

            if board[win[0] - 1] in ["x", "o"]:    return board[win[0] - 1]

    else:

        if "*" not in board:    return "DRAW"

    return False

while True:

    print(displayBoard(board))
    
    player = int(input("Enter your move (1-9): "))

    if board[player - 1] != "*":

        print("Invalid Move! Try again!")

    else:

        if count % 2 != 0:
            board[player - 1] = "x"
        else:
            board[player - 1] = "o"

        result = checkWin(board)

        if result == 'DRAW':

            print("It's a draw! Good game! 👏🏻")
            break

        elif result in ["x", "o"]:

            print(f"GAME OVER! WINNER --- {result.upper()}")
            break

        else: count += 1
