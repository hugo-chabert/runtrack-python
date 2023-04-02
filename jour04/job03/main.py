def place_queens(n):
    def is_safe(board, row, col):
        # Vérifie si une reine peut être placée en position (row, col) sur le plateau
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            # Toutes les reines ont été placées, on a trouvé une solution
            print_board(board)
            return True
        else:
            # Essaie de placer une reine dans chaque colonne de la ligne actuelle
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)
                    board[row] = -1
            return False

    def print_board(board):
        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print(" X ", end="")
                else:
                    print(" O ", end="")
            print()

    # Initialise le plateau vide
    board = [-1] * n
    # Résout le problème en plaçant les reines sur le plateau
    solve(board, 0)

# Demande à l'utilisateur de renseigner la taille du plateau de jeu
n = int(input("Entrez la taille du plateau de jeu : "))
# Place les reines sur le plateau
place_queens(n)