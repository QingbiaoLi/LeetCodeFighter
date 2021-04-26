class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def longestAtIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l + 1, l, r)

        longest = 0
        left = 0
        right = -1

        for i in range(len(s)):
            # Find the longest even length palindrome with center points as i-1 and i.
            length, l, r = longestAtIndex(s, i, i)
            if length > longest:
                longest = length
                left = l
                right = r

            # Find the longest odd length palindrome with center point as i
            length, l, r = longestAtIndex(s, i, i + 1)
            if length > longest:
                longest = length
                left = l
                right = r

        return s[left:right + 1]