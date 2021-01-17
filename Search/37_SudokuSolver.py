class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(x, y):
            tmp = board[x][y]
            board[x][y] = 'D'
            for i in range(9):
                if board[i][y] == tmp: return False
            for i in range(9):
                if board[x][i] == tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[int(x / 3) * 3 + i][int(y / 3) * 3 + j] == tmp: return False
            board[x][y] = tmp
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        dfs(board)



class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows_ = [[0] * (10) for _ in range(9)]
        cols_ = [[0] * (10) for _ in range(9)]
        boxes_ = [[0] * (10) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char != '.':
                    n = int(int(char) - 0)
                    bx = int(j/3)
                    by = int(i/3)
                    rows_[i][n] = 1
                    cols_[j][n] = 1
                    boxes_[by * 3 + bx][n] = 1

        # print(rows_)
        # print(boxes_)

        def fill(board, x, y):
            if y == 9: return True

            nx = (x + 1) % 9
            if (nx == 0):
                ny = y + 1
            else:
                ny = y

            if board[y][x] != '.':
                return fill(board, nx, ny)

            for i in range(1, 10):
                bx = int(x/3)
                by = int(y/3)
                box_key = by * 3 + bx

                if (not rows_[y][i] and not cols_[x][i] and not boxes_[box_key][i]):
                    rows_[y][i] = 1
                    cols_[x][i] = 1
                    boxes_[box_key][i] = 1
                    board[y][x] = '{}'.format(i)

                    if fill(board, nx, ny): return True
                    board[y][x] = '.'
                    boxes_[box_key][i] = 0
                    cols_[x][i] = 0
                    rows_[y][i] = 0

            return False

        fill(board, 0, 0)
        print(board)


print(Solution2().solveSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))