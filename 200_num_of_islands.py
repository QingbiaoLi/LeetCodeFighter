class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])

        answer = 0

        for y in range(row):
            for x in range(col):
                if grid[y][x] == '1':
                    answer += 1
                    self.__dfs(grid, x, y, col, row)
        return answer

    def __dfs(self, grid, x, y, col, row):

        if x < 0 or y < 0 or x >= col or y >= row or grid[y][x] == '0':
            return

        grid[y][x] = '0'
        self.__dfs(grid, x + 1, y, col, row)
        self.__dfs(grid, x - 1, y, col, row)
        self.__dfs(grid, x, y + 1, col, row)
        self.__dfs(grid, x, y - 1, col, row)



