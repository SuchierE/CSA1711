# Alpha-Beta Pruning for Tic-Tac-Toe

board = [" "] * 9


def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")


def winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in wins
    )


def alpha_beta(maximizing, alpha, beta):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if maximizing:
        best = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alpha_beta(False, alpha, beta)
                board[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alpha_beta(True, alpha, beta)
                board[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best


def best_move():
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alpha_beta(False, -float("inf"), float("inf"))
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():
    print("Tic-Tac-Toe using Alpha-Beta Pruning")
    print("You are X, Computer is O")

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

        if winner("X"):
            print_board()
            print("You win!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        move = best_move()
        board[move] = "O"
        print("Computer chooses position:", move + 1)

        if winner("O"):
            print_board()
            print("Computer wins!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break


play_game()
