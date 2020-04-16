def check_win(player, board):
    win = False
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            win = True
            break
        elif board[0][i] == board[1][i] == board[2][i] == player:
            win = True
            break
    if board[0][0] == board[1][1] == board[2][2] == player:
        win = True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        win = True
    return win


def check_state(x, o, board):
    if -1 <= (x_count - o_count) <= 1:
        win_x = check_win('X', board)
        win_o = check_win('O', board)
        cells = "".join(str(item) for row in board for item in row)
        if win_x and win_o:
            return "Impossible"
        elif win_x:
            state = "X wins"
        elif win_o:
            state = "O wins"
        elif " " in cells or "_" in cells:
            state = ""
        else:
            state = "Draw"
    else:
        state = "Impossible"
    return state


state = ""
x_turn = True
x_count = 0
o_count = 0
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("---------")
for i in range(len(board)-1, -1, -1):
    print(f"| {board[i][0]} {board[i][1]} {board[i][2]} |")
print("---------")
while True:
    c, r = input("Enter the coordinates: ").split()
    try:
        col = int(c)
        row = int(r)
        if board[row-1][col-1] == " ":
            board[row-1][col-1] = "X" if x_turn else "O"
            x_count += 1 if x_turn else 0
            o_count += 1 if not x_turn else 0
            x_turn = not x_turn
            print("---------")
            for i in range(len(board)-1, -1, -1):
                print(f"| {board[i][0]} {board[i][1]} {board[i][2]} |")
            print("---------")
            state = check_state(x_count, o_count, board)
            if state != "":
                print(state)
                break
        else:
            print("This cell is occupied! Choose another one!")
    except:
        print("You should enter numbers!")
