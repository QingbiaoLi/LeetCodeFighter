class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        strx = str(x)
        result = ''

        if (strx[0] == '-'):
            result = '-'
            strx = strx[1:]

        if len(strx) > 1:
            strx = strx.rstrip('0')

        strx = strx[::-1]

        result = result + strx

        if int(result) > 2 ** 31 - 1 or int(result) < -2 ** 31:
            return 0
        else:
            return int(result)


class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        def divide(number, divider):
            return int(number * 1.0 / divider)

        def mod(number, m):
            if number < 0:
                return number % (-m)

            return number % m

        Max_int = 2 ** 31 - 1
        Min_int = -2 ** 31

        result = 0

        while x:

            remain = mod(x, 10)
            x = divide(x, 10)
            if result > divide(Max_int, 10) or (result == divide(Max_int, 10) and remain > 7):
                return 0

            if result < divide(Min_int, 10) or (result == divide(Min_int, 10) and remain < -8):
                return 0

            result = result * 10 + remain
        return result
