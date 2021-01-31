class Solution(object):
    # 动态规划（空间优化）
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = triangle[i - 1][j - 1]
                if i == 1 and j == 1:
                    continue
                if j == 0:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
                elif j == i:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        dp = sorted(dp)
        return dp[0][0]

# 动态规划

class Solution3(object):
    def minimumTotal(self, triangle):
        m = len(triangle)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]

class Solution4(object):
    def minimumTotal(self, triangle):
        memo = {}

        def path(triangle, i, j):
            # 设置终止条件
            if i == len(triangle):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = min(path(triangle, i + 1, j), path(triangle, i + 1, j + 1)) + triangle[i][j]

            # 直接使用公式
            return memo[(i, j)]

        return path(triangle, 0, 0)


if __name__ == "__main__":
    assert Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
    #== 11