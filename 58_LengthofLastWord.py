class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        split_list = s.split()

        if len(split_list) == 0:
            return 0

        last_word = split_list[-1]

        return len(last_word)



class Solution2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.isspace():
            return 0
        words = s.split()
        if words[-1].isalpha():
            return len(words[-1])
        else:
            return 0