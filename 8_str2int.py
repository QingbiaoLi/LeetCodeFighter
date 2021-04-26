class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        Max_INT = 2 ** 31 - 1
        Min_INT = -2 ** 31

        i = 0
        result = 0
        sign = 1

        # ignore leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # check sign

        if i < len(s) and s[i] == '-':
            i += 1
            sign = -1
        elif i < len(s) and s[i] == '+':
            i += 1

        str_checkboard = set('0123456789')

        while i < len(s) and s[i] in str_checkboard:
            result = result * 10 + int(s[i])
            i += 1

        result = result * sign

        if result < 0:
            return max(result, Min_INT)
        return min(result, Max_INT)