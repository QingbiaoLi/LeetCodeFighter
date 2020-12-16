class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if (len(digits) == 0): return []

        digit2char = {'1': '', '2': 'abc', '3': 'def',
                      '4': 'ghi', '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}

        results = ['']

        for digit in digits:
            tmp = []
            for char in digit2char[digit]:
                tmp = tmp + [char_previous + char for char_previous in results]

            results = tmp

        return results