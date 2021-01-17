

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_num = len(nums)

        used = [False] * len_num
        nums.sort()
        path = []
        ans = []

        def dfs(nums, path, used, ans):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
                used[i] = True
                path.append(nums[i])

                dfs(nums, path, used, ans)
                path.pop()
                used[i] = False

        dfs(nums, path, used, ans)
        return ans


class Solution2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, path, res):
            if len(nums) == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        nums.sort()
        res = []
        dfs(nums, [], res)
        res = set(tuple(l) for l in res)
        return list(res)


if __name__ == "__main__":
    assert Solution().permuteUnique(
        [1, 1, 2]
    )
    #== 11