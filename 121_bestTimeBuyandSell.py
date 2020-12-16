class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num_list = len(prices)
        if num_list < 1: return 0

        list_min_price = [0] * num_list
        list_max_profit = [0] * num_list

        list_min_price[0] = prices[0]
        list_max_profit[0] = 0

        for i in range(1, num_list):
            list_min_price[i] = min(list_min_price[i - 1], prices[i])
            list_max_profit[i] = max(list_max_profit[i - 1], prices[i] - list_min_price[i - 1])

        return list_max_profit[num_list - 1]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num_list = len(prices)
        if num_list < 2: return 0

        list_gain = [0] * (num_list)

        for i in range(1, num_list):
            list_gain[i] = prices[i] - prices[i - 1]
        return max(0, self.maxSubArray(list_gain))

    def maxSubArray(self, subArray):

        num_subArray = len(subArray)

        list_max_subArray = [0] * num_subArray
        list_max_subArray[0] = subArray[0]

        for i in range(1, num_subArray):
            list_max_subArray[i] = max(list_max_subArray[i - 1] + subArray[i], subArray[i])

        return max(list_max_subArray)