class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        memo = [[0] * (n+1) for _ in range(m+1)]
        return self.dfs(m , n , memo)

    def dfs(self, m, n, memo):  # methods of postion m, n

        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1
        if memo[m][n]:
            return memo[m][n]
        up = self.dfs(m - 1, n, memo)
        left = self.dfs(m, n - 1, memo)
        memo[m][n] = up + left
        return memo[m][n]


class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if m < 0 or n < 0:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # if obstacleGrid[0][0] == 0:
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]