#2d array creates board shape
board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]

#Players pieces
player1 = "X"
player2 = "O"
#If this number reaches 0 then all players have used up their pieces and the game is a draw
player1Count = 5
#This will determine whos turn it is
currentPlayer = player1
#If this becomes true the game ends
winCondition = False

#prints index positions onto the board so players can see what numbers are needed to place their piece
def printIndexes():
  for row in range(0, len(board)):
    for column in range(0, len(board)):
      board[row][column] = str(row) + ":" + str(column)

#Prints the board out in correct shape
def printBoard():
  for row in board:
    print(row) 

#Input sanitisation for the row
def askForRow():
  global rowIndex
  try:
    rowIndex = int(input("Player using {} please choose a valid row ".format(currentPlayer)))
  except ValueError:
    print()
    print("Invalid character. Please use 1 or 2")
    print()
    askForRow()
  except NameError:
    print()
    print("Invalid character. Please use 1 or 2")
    print()
    askForRow()


#Input sanitisation for the column
def askForColumn():
  global columnIndex
  try:
    columnIndex = int(input("Player using {} please choose a valid column ".format(currentPlayer)))
  except ValueError:
    print()
    print("Invalid character. Please use 1 or 2")
    print()
    askForColumn()
  except NameError:
    print()
    print("Invalid character. Please use 1 or 2")
    print()
    askForColumn()


#Checks to see the position given by player to see if it is a legal move. If it is legal then it will place piece onto the board using the row and column number 
def askForPosition():
  askForRow()
  while rowIndex != 0 and rowIndex != 1 and rowIndex != 2:
    print()
    print("Invalid character. Please use 1 or 2")
    print()
    askForRow()

  askForColumn()
  while columnIndex != 0 and columnIndex != 1 and columnIndex != 2:
    print()
    print("Invalid character. Please use 1 or 2")
    print()
    askForColumn()

  if board[int(rowIndex)][int(columnIndex)] == player1 or board[int(rowIndex)][int(columnIndex)] == player2:
    print()
    print("Position has already been filled")
    print()
    askForPosition()
  else:
    board[int(rowIndex)][int(columnIndex)] = currentPlayer

#Using a bunch of if statements to see if TicTacToe win conditons or a draw has occured
def winConditions():
  global winCondition
  if board[0][0] == player1 and board[0][1] == player1 and board[0][2] == player1:
    print("Player using X wins the game!")
    winCondition = True

  elif board[0][0] == player1 and board[1][0] == player1 and board[2][0] == player1:
    print("Player using X wins the game!")
    winCondition = True
    
  elif board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1:
    print("Player using X wins the game!")
    winCondition = True
    
  elif board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1:
    print("Player using X wins the game!")
    winCondition = True

  elif board[0][2] == player1 and board[1][2] == player1 and board[2][2] == player1:
    print("Player using X wins the game!")
    winCondition = True
  
  elif board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
    print("Player using X wins the game!")
    winCondition = True

  elif board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1:
    print("Player using X wins the game!")
    winCondition = True

  elif board[0][1] == player1 and board[1][1] == player1 and board[2][1] == player1:
    print("Player using X wins the game!")

  elif board[0][0] == player2 and board[0][1] == player2 and board[0][2] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[0][0] == player2 and board[1][0] == player2 and board[2][0] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[0][0] == player2 and board[1][1] == player2 and board[2][2] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[2][0] == player2 and board[2][1] == player2 and board[2][2] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[0][2] == player2 and board[1][2] == player2 and board[2][2] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[0][2] == player2 and board[1][1] == player2 and board[2][0] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[1][0] == player2 and board[1][1] == player2 and board[1][2] == player2:
    print("Player using O wins the game!")
    winCondition = True

  elif board[0][1] == player2 and board[1][1] == player2 and board[2][1] == player2:
    print("Player using O wins the game!")
    winCondition = True
  
  elif player1Count == 0:
    print("The game ended in a draw!")
    winCondition = True

  else:
    pass

def main():
  global currentPlayer
  global player1Count

  askForPosition()
  
  if currentPlayer == player1:
    player1Count = player1Count - 1
    currentPlayer = player2
  else:
    currentPlayer = player1

  print()
  printBoard()
  print()
  winConditions()

printIndexes()
printBoard()

while winCondition == False:
   main()

