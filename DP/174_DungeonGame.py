class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])

        hp = [[float("inf")] * (n+1) for _ in range(m+1)]

        hp[m][n-1] = 1
        hp[m-1][n] = 1

        for y in range(m-1, -1, -1):
            for x in range(n-1, -1, -1):
                hp[y][x] = max(1, min(hp[y + 1][x], hp[y][x+1]) - dungeon[y][x])
                # print("(y,x) - ({},{}) - HP:{}".format(y,x,hp[y][x]))

        return hp[0][0]


if __name__ == "__main__":
    assert Solution().calculateMinimumHP(
        [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    )
    #== 11