class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)

        while (left < right):
            middle = left + (right - left) / 2

            if (nums[middle] == target):
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle + 1
        return left


