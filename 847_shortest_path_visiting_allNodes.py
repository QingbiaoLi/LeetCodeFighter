class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        import collections

        dp = [
            [float("inf")] * (len(graph))

            for _ in range(1 << len(graph))
        ]

        q = collections.deque()

        for i in range(len(graph)):
            dp[1 << i][i] = 0
            q.append((1 << i, i))

        while q:
            state, node = q.popleft()
            steps = dp[state][node]
            for cur_state in graph[node]:
                next_state = state | (1 << cur_state)

                if dp[next_state][cur_state] == float("inf"):
                    dp[next_state][cur_state] = steps + 1
                    q.append((next_state, cur_state))

        return min(dp[-1])
