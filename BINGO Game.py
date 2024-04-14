import random
board=[]

def generate():
    for i in range(5):
        b=random.sample(range(1,101),5)
        board.append(b)
    return board

def display(board):
    for i in board:
        for j in i:
            print(f"{j}", end=" ")
        print()

def marknumber(board,number):
    for i in range(5):
        for j in range(5):
            if board[i][j]==number:
                board[i][j]='X'

def usernumber():
    while True:
        try:
            number=int(input("enter n="))
            if number<=100 and number>=1:
                return number
            else:
                print("invalid input!!. Please enter value between 1 and 100")
        except ValueError:
            print("invalid input. Please enter value between 1 and 100")

def horizLines(board):
  lines = []
  for row in range(5):
    lines.append([board[row][0] , board[row][1], board[row][2], board[row][3], board[row][4]])
  return lines

def vertLines(board):
  lines = []
  for col in range(5):
    lines.append([board[0][col], board[1][col] , board[2][col], board[3][col], board[4][col]])
  return lines

def diagLines(board):
  leftDown = ([board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]])
  rightDown = ([board[4][0],  board[1][3], board[2][2], board[3][1] , board[0][4]])
  return [leftDown, rightDown]

def checkwin(board):
    all_lines=vertLines(board)+horizLines(board)+diagLines(board)
    for line in all_lines:
        if line==['X', 'X', 'X', 'X', 'X']:
            return True
    

def playBingoGame():
    print("welcome player")
    board=generate()
    display(board)
    count=0
    while not checkwin(board):
        num=usernumber()
        marknumber(board,num)
        count+=1
        display(board)
    if checkwin(board)==True:
        print("congratulations ! count: " , count)
        

playBingoGame() 
