# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#
# Tags: Backtracking, Hash Table
# Difficulty: Hard


class Solution(object):
    nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0)

    def solve(self, board, start_index):
        i = start_index
        while i < 81:
            x, y = i / 9, i % 9
            if board[x][y] == '.':
                break
            i += 1

        if i >= 81:
            return self.isValidSudoku(board)

        candidates = self.possible_nums(board, x, y)
        if not candidates:
            return False

        for num in candidates:
            board[x][y] = num
            solved = self.solve(board, i + 1)
            if solved:
                return True
            else:
                board[x][y] = '.'

        return False

    def possible_nums(self, board, x, y):
        x_start = x / 3 * 3
        y_start = y / 3 * 3
        square = (board[i][j] for i in xrange(x_start, x_start + 3) for j in xrange(y_start, y_start + 3))
        row = board[x]
        column = (board[i][y] for i in xrange(9))
        return self.nums - (set(square) | set(row) | set(column))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.valid_9_nums(board[i]):
                return False
            if not self.valid_9_nums([board[j][i] for j in xrange(9)]):
                return False

        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                digits = [board[m][n] for m in xrange(i, i+3) for n in xrange(j, j+3)]
                if not self.valid_9_nums(digits):
                    return False

        return True

    def valid_9_nums(self, digits):
        return len(set(digits)) == len(digits)


if __name__ == '__main__':
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."],
             [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    Solution().solveSudoku(board)
    for row in board:
        print row
