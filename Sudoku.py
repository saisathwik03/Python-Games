import random

lst=[[8, 9, 5, 1, 3, 2, 4, 7, 6], [7, 2, 6, 8, 4, 5, 1, 9, 3], [1, 4, 3, 6, 7, 9, 2, 8, 5], [2, 1, 4, 7, 9, 6, 5, 3, 8], [6, 7, 8, 5, 1, 3, 9, 4, 2], [3, 5, 9, 4, 2, 8, 7, 6, 1], [4, 6, 7, 2, 8, 1, 3, 5, 9], [9, 8, 1, 3, 5, 4, 6, 2, 7], [5, 3, 2, 9, 6, 7, 8, 1, 4]]
board=[]
for row in range(len(lst)):
    values=lst[row]
    # print(values)

def areLegalValues(values):
    N=int(len(values)**0.5)
    check_values=set()
    if len(values)!=N**2:
        return False
    for value in values:
        a = 0 <= value <= N**2
        if not a:
            return False
        if value!=0:
            if value in check_values:
                return False
            check_values.add(value)
    return True

# areLegalValues(values)

def gen_board():
    board=[]
    for i in range(len(lst)):
        values=lst[i]
        board.append(values)
    for row in board:
        for val in row:
            print(val, end=" ")
        print()
    return board
# lst1=[]
# gen_board()
# print(" --------------")

def isLegarRow(board,row):
    a=board[row]
    # print(a)
    if areLegalValues(a):
        return True
    else:
        return False

# board=gen_board()
# row=int(input("enter values from 0 to N**2: "))
# isLegarRow(board,row)

# print(" --------------")


def isLegalCol(board,col):
    n=len(board)
    col_values=[board[i][col] for i in range(n)]
    # print(col_values)
    if areLegalValues(col_values):
        return True
    else:
        return False     
        
# board=gen_board()
# col=int(input("enter col value from 0 to 8: "))
# isLegalCol(board,col)

# print(" --------------")

def isLegalBlock(board, block):
    n = len(board)
    block_size = int(n ** 0.5)
    block_val=[]

    row_begin = (block // block_size) * block_size
    col_begin = (block % block_size) * block_size
    
    a=row_begin + block_size
    b=col_begin + block_size

    for row in range(row_begin,a):
        for col in range(col_begin, b):
            block_val.append(board[row][col])
    # print(block_val)

    return areLegalValues(block_val)

# board = gen_board()  
# block = int(input("Enter the block number (0 to 8): "))
# isLegalBlock(board, block)

def isLegalSudoku(board):
    n=len(board)
    for row in range(n):
        if not isLegarRow(board,row):
            return False
    for col in range(n):
        if not isLegalCol(board,col):
            return False
    block_size=int(n**0.5)
    for block in range(n):
        if not isLegalBlock(board,block):
            return False
    return True

board=gen_board()
print(isLegalSudoku(board))