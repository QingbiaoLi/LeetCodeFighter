class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt, total = 0, 0
        cache = {0: 1}
        for v in nums:
            total += v
            if cache.get(total-k):
                cnt += cache[total-k]
            if cache.get(total):
                cache[total] += 1
            else:
                cache[total] = 1
        return cnt


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 9
    # assert (Solution().twoSum(nums, target) == [0, 1])
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))