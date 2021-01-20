class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '': return ""
        ans = ''

        i = 0
        len_Str = len(s)
        c = 0
        while s[i].isdigit() and i < len_Str:
            c = c*10 + int(int(s[i]) - 0)
            i = i+1

        j = 1
        if i <len_Str and s[i] =='[':
            open = 1
            while j < len_Str and open:
                if s[j] =='[':
                    open += 1
                elif s[j] == ']':
                    open -= 1
                j += 1
        else:
            while (j<len_Str and s[j].isalpha()):
                j += 1

        if i == 0:
            return s[0:j] + self.decodeString(s[j:])

        sub_str = self.decodeString(s[i+1: j - i - 2])

        while c:
            ans += sub_str
            c -= 1

        ans += self.decodeString(s[j:])

        return ans

class Solution2(object):
    def decodeString(self, s):
        num = 0
        string = ''
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            elif c.isalpha():
                string += c
            elif c == ']':
                pre_num = stack.pop()
                pre_string = stack.pop()
                string = pre_string + pre_num * string
        return string

if __name__ == "__main__":
    # a = Solution()
    # a.countOfAtoms("K4(ON(SO3)2)2")
    a = Solution2()
    print(a.decodeString("3[a]2[bc]"))
