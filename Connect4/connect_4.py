def initialize_grid():
    board = []
    for row in range(6):
        row = []
        for col in range(7):
            row.append(0)
        board.append(row)
    return board

def print_grid(board):
    for row in range(6):
        for col in range(7):
            print(board[row][col], end=' ')
        print()

def get_user_input():
    col = input("Enter the column number to drop your disc (0-6): ")
    if col.isdigit():
        col = int(col)
        if 0 <= col <= 6:
            return col
        else:
            return 'Please enter a column number between 0 and 6 only!'
    else:
        return 'Enter a valid input, only numbers!!!'

def drop_disc(board, col, disc):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = disc
            break  
    return board

def check_win(board):
    #Horizontal-check
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != 0:
                return True
    
    #Vertical-check
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != 0:
                return True
            
    #Diagnol-check +ve slope
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != 0:
                return True
            
    #Diagnol-check -ve slope
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != 0:
                return True
    return False

def check_draw(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == 0:
                return False
    
    if not check_win(board):
        return True
    return False

def switch_player(current_player):
    if current_player == 1:
        return 2
    else:
        return 1

def play_game():
    print("Welcome to Connect-4 game!!!")
    board = initialize_grid()
    current_player = 1
    
    while True:
        print_grid(board)
        col = get_user_input()
        board = drop_disc(board, col, current_player)
        
        if check_win(board):
            print_grid(board)
            print("Player", current_player, "Wins!!")
            break
        elif check_draw(board):
            print_grid(board)
            print("The game is a draw!!")
            break

        current_player = switch_player(current_player)

play_game()