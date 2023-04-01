from Board import Board

board = Board(6, 7)

def check_win(board, color):
    # Check horizontale
    for i in range(board.i):
        for j in range(board.j-3):
            if board.board[i][j] == color and board.board[i][j+1] == color and board.board[i][j+2] == color and board.board[i][j+3] == color:
                return True

    # Check verticale
    for i in range(board.i-3):
        for j in range(board.j):
            if board.board[i][j] == color and board.board[i+1][j] == color and board.board[i+2][j] == color and board.board[i+3][j] == color:
                return True

    # Check diagonale \
    for i in range(board.i-3):
        for j in range(board.j-3):
            if board.board[i][j] == color and board.board[i+1][j+1] == color and board.board[i+2][j+2] == color and board.board[i+3][j+3] == color:
                return True

    # Check diagonale reverse /
    for i in range(3, board.i):
        for j in range(board.j-3):
            if board.board[i][j] == color and board.board[i-1][j+1] == color and board.board[i-2][j+2] == color and board.board[i-3][j+3] == color:
                return True

    return False

turn = 0
while True:
    board.print()
    if turn % 2 == 0:
        player_color = "J"
        player_name = "Joueur 1"
    else:
        player_color = "R"
        player_name = "Joueur 2"

    column = int(input(player_name + " (" + player_color + "): Choisis une numéro de la colonne ou tu veux jouer (0-" + str(board.j-1) + "): "))

    if board.play(column, player_color):
        if check_win(board, player_color):
            board.print()
            print(player_name + " est le Vainqueur ! Il gagne donc 100 000€")
            break

        turn += 1
        if turn == board.i * board.j:
            board.print()
            print("Egalité !")
            break