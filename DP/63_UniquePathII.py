class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        return self.dfs(m - 1, n - 1, obstacleGrid, memo)

    def dfs(self, m, n, obstacleGrid, memo):  # methods of postion m, n
        if obstacleGrid[m][n] == 1:
            return 0
        if m < 0 or n < 0:
            return 0
        if m == n == 0:
            return 1
        if memo[m][n]:
            return memo[m][n]
        up = self.dfs(m - 1, n, obstacleGrid, memo)
        left = self.dfs(m, n - 1, obstacleGrid, memo)
        memo[m][n] = up + left
        return memo[m][n]



class Solution2(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i != 0:
                        dp[i][j] += dp[i - 1][j]
                    if j != 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]