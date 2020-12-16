class Solution(object):
    def maxSubArray(self, subArray):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## solution 1
        num_subArray = len(subArray)

        list_max_subArray = [0] * num_subArray
        list_max_subArray[0] = subArray[0] # ensure > 0

        for i in range(1, num_subArray):
            list_max_subArray[i] = max(list_max_subArray[i - 1] + subArray[i], subArray[i])

        return max(list_max_subArray)


class Solution(object):
    def maxSubArray(self, subArray):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## solution 1
        import copy
        num_subArray = len(subArray)

        answer = copy.deepcopy(subArray[0])
        sum_value = copy.deepcopy(subArray[0])

        for i in range(1, num_subArray):
            sum_value = max(sum_value + subArray[i], subArray[i])

            if (sum_value > answer):
                answer = sum_value

        return answer