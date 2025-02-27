class Piece:
    def __init__(self, symbol, color='white',  is_king=False, position=False,):
        self.symbol = symbol # this is the actual board sympol
        if self.symbol == '⚇' or self.symbol == '⚉': # set the "is king"
            self.is_king = True
        else:
            self.is_king = False
        if self.symbol == '⚈' or self.symbol == '⚉':  # set the color
            self.color = 'black'
        else:
            self.color = color

    def spaces_to_check(self, i, j, board): # spaces to check to see if there is an available move, if black checking down the board, if white up the board, if king in both directions
        spaces_to_check = []
        if self.color == 'black' or self.is_king:
            if i < len(board) - 1:
                if j > 0:
                    spaces_to_check.append([board[i + 1][j - 1], [i + 1, j - 1]])
                if j < len(board[0]) -1:
                    spaces_to_check.append([board[i + 1][j + 1], [i + 1, j + 1]])
        elif self.color == 'white' or self.is_king:  # if the piece is white
            if i > 0:
                if j > 0:
                    spaces_to_check.append([board[i - 1][j - 1], [i - 1, j - 1]])
                if j < len(board[0]) - 1:
                    spaces_to_check.append([board[i - 1][j + 1], [i - 1, j + 1]])
        return spaces_to_check

    def __repr__(self):
        return self.symbol # print out the symbol associated with this piece

