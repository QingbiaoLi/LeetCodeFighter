class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        # key = starting element of an AP,
        # value = length of AP
        memo = dict()

        # since the length of longest AP is at least
        # one i.e. the number itself.
        maxt = 1

        len_arr = len(arr)

        # if element a[i]'s starting element(i.e., a[i]-i*d)
        # is not in map then its value is 1 else there already
        # exists a starting element of an AP of which a[i]
        # can be a part.
        for i in range(len_arr):
            if (arr[i] - difference) in memo:
                memo[arr[i]] = memo[arr[i]-difference] + 1
            else:
                memo[arr[i]] = 1
        # # In this it variable will be
        # # # storing key value of dictionary.
        for it in memo:
            if memo[it] > maxt:
                # calculating the length of longest AP.
                maxt = memo[it]

        return maxt


if __name__ == "__main__":
    difference = -2
    a = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    find_sol = Solution()
    print(find_sol.longestSubsequence(arr=a, difference=difference))