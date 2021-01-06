solution = []

def isSafe(board, row, col):
  for i in range(len(board)):
    if board[row][i] == 1:
      return False
  
  for i in range(len(board)):
    if board[i][col] == 1:
      return False
  
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  
  for i, j in zip(range(row, -1, -1), range(col, len(board))):
    if board[i][j] == 1:
      return False

  return True


def solve(board, row):
  if row >= len(board):
    solution.append(board)
    printboard(board)
    print()

  else:
    for i in range(len(board)):
      if isSafe(board, row, i):
        board[row][i] = 1
        solve(board, row+1)
        board[row][i] = 0
  return False

def printboard(board):
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 1:
        print('Q', end=' ')
      else:
        print('.', end=' ')
    print()

n = 8 
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
