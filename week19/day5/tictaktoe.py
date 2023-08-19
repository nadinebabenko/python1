#Create a TicTacToe game in python, where two users can play together.

class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_player = 'X'

    def display_board(self):
        print('-------------')
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    def get_move(self):
        while True:
            try:
                row = int(input('Enter row (1-3): ')) - 1
                col = int(input('Enter column (1-3): ')) - 1
                if self.board[row][col] == ' ':
                    return row, col
                else:
                    print('That position is already taken.')
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 3.')

    def make_move(self, row, col):
        self.board[row][col] = self.current_player

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_tie(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        while True:
            self.display_board()
            print(f"It's {self.current_player}'s turn.")
            row, col = self.get_move()
            self.make_move(row, col)
            if self.check_win():
                self.display_board()
                print(f'{self.current_player} wins!')
                break
            elif self.check_tie():
                self.display_board()
                print('Tie game!')
                break
            self.switch_player()
game = TicTacToe()
game.play()