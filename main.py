def check_winner(board):
    # Define the function to check if there's a winner

    # List of possible winning combinations in a game of Tic Tac Toe
    win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
                        (1, 5, 9), (3, 5, 7)]  # diagonals
    for combination in win_combinations:
        # Check if all positions in the current combination are occupied by the same player and are not empty
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != "-":
            return board[combination[0]]
    return None

def print_board(board):
    for i in [7, 4, 1]:
        print(" | ".join(board[i:i+3]))

def play_game():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        position = int(input("Enter a position (1-9): "))

        # Check if the position is already occupied
        if board[position] != "-":
            print("This position is already occupied. Try again.")
            continue

        board[position] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)  # Print the board before announcing the winner
            print(f"Player {winner} wins!")
            game_over = True

        current_player = "O" if current_player == "X" else "X"

play_game()