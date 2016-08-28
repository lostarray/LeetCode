# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules (http://sudoku.com.au/TheRules.aspx).
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
#
# Tags: Hash Table
# Difficulty: Easy


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.valid(board[i]):
                return False
            if not self.valid((board[j][i] for j in xrange(9))):
                return False

        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                strs = (board[m][n] for m in xrange(i, i+3) for n in xrange(j, j+3))
                if not self.valid(strs):
                    return False

        return True

    def valid(self, strs):
        digits = [s for s in strs if s != '.']
        return len(set(digits)) == len(digits)
