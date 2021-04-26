class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def canBreak(s, m, wordDict):
            if s in m: return m[s]

            if s in wordDict:
                m[s] = True
                return True

            for i in range(1, len(s)):
                r = s[i:]

                if r in wordDict and canBreak(s[0:i], m, wordDict):
                    m[s] = True
                    return True

            m[s] = False
            return False

        return canBreak(s, {}, set(wordDict))


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 9
    # assert (Solution().twoSum(nums, target) == [0, 1])

    # s = "leetcode"
    # wordDict = ["leet", "code"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))