class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2: return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]



class Solution2(object):
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n):


        if n < 3:
            return n
        else:
            return self._climbStairs(n - 1) + self._climbStairs(n - 2)

    def _climbStairs(self, n):
        if n not in self.cache.keys():
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]

class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        else:
            res, step_1, step_2 = 0, 1, 2
            for i in range(2, n):
                res = step_2 + step_1
                step_1 = step_2
                step_2 = res
            return res