import random

print("Welcome to Connect Four")
print("------------------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)] 


rows = 6
cols = 7

def printgameBoard():
    print("\n    A    B    C    D    E    F    G " ,end="")
    for x in range(rows):
        print ("n\ +----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
               print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
               print("", gameBoard[x][y], end=" |")
            else:
               print(" ", gameBoard[x][y], end=" |")
        # print()
    print("\n +----+----+----+----+----+----+")

printgameBoard()

# import random

# print("Welcome to Connect Four")
# print("-----------------------")

# possibleLetters = ["A","B","C","D","E","F","G"]
# gameBoard = [["" for _ in range(7)] for _ in range(6)]  # Creating a 6x7 game board

# rows = 6
# cols = 7

# def printGameBoard():
#     print("\n    A    B    C    D    E    F    G ")
#     for x in range(rows):
#         print("  +----+----+----+----+----+----+")
#         print(x, " |", end="")
#         for y in range(cols):
#             if gameBoard[x][y] == "🔵":
#                print("", gameBoard[x][y], end=" |")
#             elif gameBoard[x][y] == "🔴":
#                print("", gameBoard[x][y], end=" |")
#             else:
#                print(" ", gameBoard[x][y], end=" |")
#         print()
#     print("  +----+----+----+----+----+----+")

# printGameBoard()



