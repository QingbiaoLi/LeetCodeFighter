class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]
        return self.find_sol(grid, n - 1, m - 1, n, m, memo)

    def find_sol(self, grid, x, y, n, m, memo):  # methods of postion m, n
        if x == y == 0:
            return grid[y][x]

        if x < 0 or y < 0:
            return float("inf")

        if memo[y][x] > 0:
            return memo[y][x]

        memo[y][x] = grid[y][x] + min(self.find_sol(grid, x-1, y, n, m, memo), self.find_sol(grid, x, y-1, n, m, memo))
        return memo[y][x]


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        cost = [[0] * n for _ in range(m)]


        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cost[0][0] = grid[0][0]

                if i == 0:
                    cost[i][j] = grid[i][j] + cost[i][j-1]
                elif j == 0:
                    cost[i][j] = grid[i][j] + cost[i - 1][j]
                else:
                    cost[i][j] = grid[i][j] + min(cost[i - 1][j], cost[i][j-1])


        return cost[m-1][n-1]