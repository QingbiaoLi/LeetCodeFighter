class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_num = len(nums)
        ans = []
        used = [False] * len_num

        path = []

        def dfs(index):
            if index == len_num:
                ans.append(path[:])
                return
            for i in range(len_num):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                dfs(index + 1)
                path.pop()
                used[i] = False

        dfs(0)
        return ans


class Solution(object):
    def combination(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_num = len(nums)
        ans = []

        path = []

        def dfs(index, start):
            if index == len_num:
                ans.append(path[:])
                return
            for i in range(start, len_num):

                path.append(nums[i])
                dfs(index + 1, i+1)
                path.pop()

        dfs(0, 0)
        return ans