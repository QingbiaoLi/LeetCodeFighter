class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = [''] * numRows
        rowIndex = 0
        direction = 1

        for id_str in range(len(s)):

            result[rowIndex] = result[rowIndex] + s[id_str]

            if direction == 1 and rowIndex < numRows - 1:
                rowIndex += 1

            elif direction == -1 and rowIndex > 0:
                rowIndex -= 1

            else:

                direction *= -1
                rowIndex += direction

        return ''.join(result)