class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check rows
        for i in xrange(9):
            if board[i].count('.') + len(set(board[i])) - 1 != 9:
                return False
        # check columns
        for i in xrange(9):
            col = [board[j][i] for j in xrange(9)]
            if col.count('.') + len(set(col)) - 1 != 9:
                return False
        # check 3x3 squares
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[i + m][j + n]
                          for m in (0, 1, 2)
                          for n in (0, 1, 2)]
                if square.count('.') + len(set(square)) - 1 != 9:
                    return False
        return True
