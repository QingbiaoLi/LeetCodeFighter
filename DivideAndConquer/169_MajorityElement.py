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


## HashTable
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}

        len_num = len(nums)
        for num in nums:
            # print(count[num])
            if num in num_count:
                num_count[num] = num_count[num] + 1
            else:
                num_count[num] = 1

        for num in num_count:
            if num_count[num] > len_num/2:
                return num
        return -1


## BST
class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}

        return -1


# Boyer–Moore majority vote
class Solution4(object):
    def majorityElement(self, nums):

        # m stores majority element if present
        m = -1

        # initialize counter i with 0
        i = 0

        # do for each element A[j] of the list
        for j in range(len(nums)):

            # if the counter i becomes 0
            if i == 0:

                # set the current candidate to A[j]
                m = nums[j]

                # reset the counter to 1
                i = 1

            # else increment the counter if A[j] is current candidate
            elif m == nums[j]:
                i = i + 1

            # else decrement the counter if A[j] is not current candidate
            else:
                i = i - 1

        return m

## Fully sorted
class Solution5(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedlist_nums = sorted(nums)

        return sortedlist_nums[int(len(nums)/2)]



## Divide and Conquer -- bug
class Solution6(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = self.majorityElement_divide(nums, 0, len(nums)-1)
        return ans['num']

    def majorityElement_divide(self, nums, left, right):

        if left == right:
            return {"num": nums[left], "count": 1}

        middle = int((left + right)/2)

        middleLeft = self.majorityElement_divide(nums, left, middle)
        middleRight = self.majorityElement_divide(nums, middle+1, right)

        if middleLeft == middleRight:
            return {"num": middleLeft["num"], "count": middleLeft["count"]}

        if middleLeft["count"]> middleRight["count"]:
            tmp_list = nums[middle: middle + right]
            return {"num": middleLeft["num"], "count": middleLeft["count"] + tmp_list.count(middleLeft["num"])}
        else:
            tmp_list = nums[left: middle]
            return {"num": middleLeft["num"], "count": middleLeft["count"] + tmp_list.count(middleRight["num"])}

## Divide and Conquer v2

class Solution7(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = self.majorityElement_divide(nums, 0, len(nums)-1)
        return ans

    def majorityElement_divide(self, nums, left, right):
        print(nums,left, right)

        if left == right:
            # return {"num": nums[left], "count": 1}
            return nums[left]
        middle = int((left + right)/2)

        middleLeft = self.majorityElement_divide(nums, left, middle)
        middleRight = self.majorityElement_divide(nums, middle+1, right)

        if middleLeft == middleRight:
            return middleLeft

        tmp_list_left = nums[left: middle]
        tmp_list_right = nums[middle+1: right]

        print("list_left", tmp_list_left, middleLeft)
        print("list_right", tmp_list_right, middleRight)

        if self.list_count(tmp_list_left, middleLeft) > self.list_count(tmp_list_right, middleRight):
            return middleLeft
        else:
            return middleRight

    def list_count(self, list_data, value):
        result = 0
        for data in list_data:
            if data == value:
                result+=1
        return result

if __name__ == "__main__":
    # a = Solution()
    # a.countOfAtoms("K4(ON(SO3)2)2")
    a = Solution7()
    # print(a.majorityElement([2,2,1,1,1,2,2]))
    print(a.majorityElement([8,8,7,7,7]))