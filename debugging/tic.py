def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] != " ":
                return True

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != " ":
            return True

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != " ":
            return True

    return False


def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def get_position(player):
    while True:
        try:
            row = int(input(
                "Enter row (0, 1, or 2) for player " + player + ": "
            ))
            col = int(input(
                "Enter column (0, 1, or 2) for player " + player + ": "
            ))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Please enter numbers from 0 to 2.")
            else:
                return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while not check_winner(board) and not board_full(board):
        print_board(board)

        row, col = get_position(player)

        if board[row][col] == " ":
            board[row][col] = player

            if check_winner(board):
                break

            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)

    if check_winner(board):
        print("Player " + player + " wins!")
    else:
        print("It's a draw!")


tic_tac_toe()
