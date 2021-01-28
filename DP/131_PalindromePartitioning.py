class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        result = []
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                for r in self.partition(s[i + 1:]):
                    result.append([s[:i + 1]] + r)
        return result

    def isPalindrome(self, s):
        return s == s[::-1]


class Solution2(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.isPalindrome = lambda s: s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):  # 注意起始和结束位置
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])
