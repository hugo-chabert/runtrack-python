class Board:
    def __init__(self, i, j):
        self.board = [["O" for _ in range(j)] for _ in range(i)]
        self.i = i
        self.j = j

    def play(self, column, color):
        if column < 0 or column >= self.j:
            return False
        for i in range(self.i-1, -1, -1):
            if self.board[i][column] == "O":
                self.board[i][column] = color
                return True
        print("Column is full")
        return False

    def print(self):
        for i in range(self.i):
            for j in range(self.j):
                print(self.board[i][j], end=" ")
            print()