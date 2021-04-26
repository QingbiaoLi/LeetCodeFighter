class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)

        memo = [[0 for i in range(n + 1)] for j in range(K + 1)]

        value_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            value_sum[i] = value_sum[i - 1] + A[i - 1]
        return self.LargestSumAverage(A, value_sum, memo, n, K)

    def LargestSumAverage(self, A, value_sum, memo, n, k):

        if memo[k][n] > 0: return memo[k][n]

        if k == 1: return 1.0 * value_sum[n] / n

        for i in range(k - 1, n):
            memo[k][n] = max(memo[k][n], self.LargestSumAverage(A, value_sum, memo, i, k - 1) + 1.0 * (
                        value_sum[n] - value_sum[i]) / (n - i))

        return memo[k][n]


class Solution2(object):
    def largestSumOfAverages(self, A, K):
        N = len(A)
        S = [0] * (N + 1)
        for x, a in enumerate(A):
            S[x + 1] += S[x] + a

        dp = [1.0 * S[x] / x for x in range(1, N + 1)]
        for x in range(K - 1):
            dp0 = [0] * N
            for y in range(x, N):
                for z in range(x, y):
                    dp0[y] = max(dp0[y], dp[z] + 1.0 * (S[y + 1] - S[z + 1]) / (y - z))
            dp = dp0
        return dp[-1]