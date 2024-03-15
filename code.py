import random

print("Welcome to Connect Four")
print("---------------------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)] 

rows = 6
cols = 7

def printgameBoard():
    print("\n      A    B    C    D    E    F    G ")
    for x in range(rows):
        print ("   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
               print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
               print("", gameBoard[x][y], end=" |")
            else:
               print("  ", gameBoard[x][y], end=" |")
        print()
    print("   +----+----+----+----+----+----+----+")

def check_win(board, piece):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True

    # Check positively sloped diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True

    # Check negatively sloped diagonals
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == piece and board[row+1][col-1] == piece and board[row+2][col-2] == piece and board[row+3][col-3] == piece:
                return True

    return False

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == ""

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == "":
            return r

def main():
    printgameBoard()
    game_over = False
    turn = 0

    while not game_over:
        # Player 1 input
        if turn == 0:
            col = int(input("Player 1 make your selection (0-6): "))
            if is_valid_location(gameBoard, col):
                row = get_next_open_row(gameBoard, col)
                drop_piece(gameBoard, row, col, "🔵")

                if check_win(gameBoard, "🔵"):
                    print("Player 1 wins!")
                    game_over = True
            else:
                print("Column is full. Please try again.")
                continue

        # Player 2 input
        else:
            col = int(input("Player 2 make your selection (0-6): "))
            if is_valid_location(gameBoard, col):
                row = get_next_open_row(gameBoard, col)
                drop_piece(gameBoard, row, col, "🔴")

                if check_win(gameBoard, "🔴"):
                    print("Player 2 wins!")
                    game_over = True
            else:
                print("Column is full. Please try again.")
                continue

        printgameBoard()
        turn += 1
        turn %= 2

if __name__ == "__main__":
    main()
