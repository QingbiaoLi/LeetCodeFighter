class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([i**2 for i in nums])



class Solution2(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1

        list_result = []

        while start <= end:
            if abs(nums[start]) >= abs(nums[end]):
                list_result.append(nums[start] * nums[start])
                start += 1
            else:
                list_result.append(nums[end] * nums[end])
                end -= 1
        list_result.reverse()
        return list_result