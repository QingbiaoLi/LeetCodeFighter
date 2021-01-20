class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0

        majorNum = nums[0]
        for num in nums:
            if vote > 0:
                if num == majorNum:
                    vote = vote + 1
                else:
                    vote = vote - 1
            if vote == 0:
                majorNum = num
                vote = 1

        return majorNum


if __name__ == "__main__":
    # a = Solution()
    # a.countOfAtoms("K4(ON(SO3)2)2")
    a = Solution()
    print(a.majorityElement([2,2,1,1,1,2,2]))