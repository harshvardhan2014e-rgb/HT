board = ['1', '2', '3',
         '4', '5', '6',
         '7','8', '9']

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winners(player):
    win_postions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for position in win_postions:
        if (board[position[0]] == board[position[1]] ==
                board[position[2]] == player):
            return True
    return False

def is_draw():
    for cell in board:
        if cell not in ['X', '0']:
            return False
        return True

player = 'X'

while True:
    display_board()

    choice = int(input(f"Player {player}, enter a postion (1-9): "))

    if choice < 1 or choice > 9:
        print("Invaild Choice! try Again!")
        continue

    if board[choice - 1] == 'X' or board[choice - 1] == '0':
        print("Postion Already Take try Again")
        continue

    board[choice - 1] == player

    if check_winners(player):
        display_board
        print(f"Player {player} wins!")
        break

    if is_draw():
        display_board()
        print("Its A Draw!")
        break

    if player == 'X' :
        player = '0'
    else:
        player = 'X'