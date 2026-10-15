import random

board = [" "] * 9


def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")


def check_winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def play_game():
    print("Tic-Tac-Toe Game")
    print("Positions are numbered 1 to 9.")

    while True:
        print_board()

        try:
            move = int(input("Enter position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        available = [i for i in range(9) if board[i] == " "]
        move = random.choice(available)
        board[move] = "O"
        print("Computer chooses position:", move + 1)

        if check_winner("O"):
            print_board()
            print("Computer wins!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break


play_game()
