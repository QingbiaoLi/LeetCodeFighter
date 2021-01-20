class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while (i < j):
            sum_value = numbers[i] + numbers[j]
            if sum_value == target:
                break
            elif sum_value < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]


class Solution2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        len_num = len(numbers)
        for i in range(len_num):
            left = i + 1
            right = len_num - 1

            remainder = target - numbers[i]

            while (left <= right):
                middle = left + (right - left)//2

                if numbers[middle] == remainder:
                    return [i+1, middle+1]

                elif numbers[middle] < remainder:
                    left = middle + 1

                else:
                    right = middle -1
        # return []

class Solution4(object):
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

class Solution3(object):
    def twoSum(self, numbers, target):
        visited = {}
        for index, number in enumerate(numbers):
            if target - number in visited:
                return [visited[target-number], index+1]
            else:
                visited[number] = index + 1