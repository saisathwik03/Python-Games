"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test


project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4

'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data['rows']=10
    data['cols']=10
    data['boardsize']=500
    data['cellsize']= data['boardsize']/ data['rows']
    data['user']=emptyGrid(data['rows'],data['cols'])
    data['computer']=emptyGrid(data['rows'],data['cols'])
    data['userships']=0
    data['computerships']=5
    data['computerboard']=addShips(data['computer'],data['computerships'])
    data['userboard']=addShips(data['user'],data['userships'])
    data["tempship"]=[]
    data['winner']=None
    data['maxturns']=50
    data['minturns']=0
    return data


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data['computerboard'],showShips=False)
    drawGrid(data,userCanvas,data["userboard"],showShips=True)
    drawShip(data,userCanvas,data["tempship"])
    drawGameOver(data,canvas=userCanvas)
    return None


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym=="Return":
       makeModel(data)
    return None


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if board=="user":
        if data["userships"]<5:
            cell=getClickedCell(data,event)
            if cell is not None:
                clickUserBoard(data,cell[0],cell[1])
        else:
            print("you are ready placed 5 ships")
    elif board=="comp" and data['userships']==5:
        cell=getClickedCell(data,event)
        if cell is not None:
            runGameTurn(data,cell[0],cell[1],'user')

#### STAGE 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(EMPTY_UNCLICKED)
        grid.append(row)       
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    cell=[]
    row=random.randint(1,8)
    col=random.randint(1,8)
    num=random.randint(0,1)

    if num==0:
        cell.append([row-1,col])
        cell.append([row,col])
        cell.append([row+1,col])
    elif num==1:
        cell.append([row,col-1])
        cell.append([row,col])
        cell.append([row,col+1])
    return cell


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    #i is coordinate
    for i in ship:
        m,n=i
        if grid[m][n]!=EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count_of_ships=0
    while numShips > count_of_ships:
        c=createShip()
        if checkShip(grid,c):
            for i in c: 
                m,n=i
                grid[m][n]=SHIP_UNCLICKED
            count_of_ships+=1
    return grid 


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    cellsize=data['cellsize']
    for i in range(data['rows']):
        for j in range(data['cols']):
            x1,y1=j*cellsize, i*cellsize
            x2,y2=x1+cellsize, y1+cellsize

            if grid[i][j]==SHIP_UNCLICKED and showShips==True:
                color="yellow"
            elif grid[i][j]==EMPTY_UNCLICKED :
                color="blue"
            elif grid[i][j]==SHIP_CLICKED:
                color="red"
            elif grid[i][j]==EMPTY_CLICKED:
                color="white"
            elif grid[i][j]==SHIP_UNCLICKED and showShips==False:
                color="blue"
            
            canvas.create_rectangle(x1,y1,x2,y2,fill=color)


### STAGE 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    # Check if all coordinates share the same column
    column = ship[0][1]   # Get the column of the first coordinate
    for i in ship:
        if i[1] != column:
            return False

    # Check if each coordinate is 1 row away from the next part
    for i in range(len(ship) - 1):
        if abs(ship[i+1][0]) - abs(ship[i][0]) != 1:
            return False
    return True
    ship.sort()
    # if ship[0][1]==ship [1][1]==ship[2][1]:
    #     if abs(ship[0][0]-ship[1][0])== abs(ship[1][0]-ship[2][0])==1:
    #         return True
    # return False
    


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    # ship.sort()
        # Check if all coordinates share the same row
    row = ship[0][0]
    for i in ship[1:]:
        if i[0] != row:
            return False
    
    # Check if all coordinates are each 1 column away from the next part
    for i in range(len(ship)-1):
        if abs(ship[i+1][1]) - abs(ship[i][1]) != 1:
            return False
    return True
    
    # ship.sort()
    # if ship[0][0]==ship[1][0]==ship[2][0]:
    #    if abs(ship[0][1]-ship[1][1])==abs(ship[1][1]-ship[2][1])==1:
    #      return True
    # return False




'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x, y = event.x, event.y
    cellsize = data["cellsize"]
    numRows, numCols = data["rows"], data["cols"]


    for row in range(numRows):
        for col in range(numCols):
            left = col * cellsize
            top = row * cellsize
            right = left + cellsize
            bottom = top + cellsize

            if left <= x <= right and top <= y <= bottom:
                return [row, col]
    return  None

    # cell_size=data["cellsize"]
    # row=int(event.y//cell_size)
    # col=int(event.x//cell_size)
    # return [row,col]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    cellsize=data["cellsize"]
    for i in ship:
        x,y=i
        x1 = y* cellsize
        y1 = x * cellsize
        x2 = x1 + cellsize
        y2 = y1 + cellsize
        canvas.create_rectangle(x1, y1, x2, y2, fill="white")


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship)!=3:
        return False
    for i in ship:
        m,n=i
        if grid[m][n]==SHIP_UNCLICKED:
               return False
    if not (checkShip(grid,ship) or (isVertical(ship) and  isHorizontal(ship))):
        return False
    return True


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["userboard"], data["tempship"]):
        for i, j in data["tempship"]:
            data["userboard"][i][j] = SHIP_UNCLICKED  
        data["userships"] += 1
        if data["userships"] == 5:
            print("You have placed 5 ships.")
        else:
            print("Ship placement successful.")
        data["tempship"] = []
    else:
        print("Invalid ship placement.")
        data["tempship"] = []


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["userships"]>=5:
         print("you have already placed 5 ships.")
         return
    if [row,col] in data["tempship"]:
        return
    data["tempship"].append([row,col])
    if len(data["tempship"])==3:
        placeShip(data)
    



### STAGE 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board[row][col]=SHIP_CLICKED
        if isGameOver(board):
            data['winner']=player
    elif board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col,player):
    if data['computerboard'][row][col]==SHIP_CLICKED or data['computerboard'][row][col]==EMPTY_CLICKED:
        return 
    else:
        updateBoard(data,data['computerboard'], row, col,player='user')
    computer_guess=getComputerGuess(data['userboard'])
    updateBoard(data,data['userboard'], computer_guess[0], computer_guess[1],player='comp')  
    data['minturns']+=1

    if data['minturns']==data['maxturns']:
        data['winner']='draw'


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    while True:
        row=random.randint(1,8)
        col=random.randint(1,8)
        if board[row][col]==SHIP_CLICKED or board[row][col]==EMPTY_CLICKED:
             continue
        else:
            return [row,col] 


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in board:
        for col in row:
            if col==SHIP_UNCLICKED:
                return False         
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == "user":
        canvas.delete("all")
        canvas.create_text(300, 40, text="CONGRATULATIONS!!! YOU'VE WON THE GAME", fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="red")
    elif data["winner"] == "comp":
        canvas.delete("all")
        canvas.create_text(300, 40, text="SORRY, YOU LOST TO THE COMPUTER", fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="red")
    elif data["winner"] == "draw":
        canvas.delete("all")
        canvas.create_text(300, 40, text="YOU'RE OUT OF MOVES AND REACHED THE DRAW", fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="red")



### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    # print("\n" + "#"*15 + " STAGE 1 TESTS " +  "#" * 16 + "\n")
    # test.stage1Tests()
    # test.testEmptyGrid()
    # test.testCreateShip()
    # test.testCheckShip()
    # test.testAddShips()
    # test.testGrid()


    ## Uncomment these for STAGE 2 ##

    # print("\n" + "#"*15 + " STAGE 2 TESTS " +  "#" * 16 + "\n")
    # test.stage2Tests()
    # test.testIsVertical()
    # test.testIsHorizontal()

    # test.testGetClickedCell()
    # test.testShipIsValid()
    

    ## Uncomment these for STAGE 3 ##
    
    # print("\n" + "#"*15 + " STAGE 3 TESTS " +  "#" * 16 + "\n")
    # test.stage3Tests()
    # test.testUpdateBoard()
    # test.testGetComputerGuess()
    # test.testIsGameOver()
    # test.testDrawGameOver()
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
