class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        len_S = len(S)
        return self.score(S, 0, len_S - 1)

    def score(self, S, left, right):
        if (right - left == 1):
            return 1

        b = 0
        for i in range(1, right):
            if S[i] == '(':
                b += 1

            if S[i] == ')':
                b -= 1

            if (b == 0):
                return self.score(S, left, i) + self.score(S, i + 1, right)

            return 2 * self.score(S, left + 1, right - 1)

class Solution2(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        len_S = len(S)
        ans = 0
        num_of_open = -1

        for i in range(len_S):
            if S[i] == '(':
                num_of_open += 1
            else:
                num_of_open -= 1

            if S[i] =='(' and S[i+1] == ')':
                ans += 2**num_of_open

        return ans




### Approach Divice and Conquer

class Solution2(object):
    def scoreOfParentheses(self, S):
        def F(i, j):
            #Score of balanced string S[i:j]
            ans = bal = 0

            #Split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i+1, k)
                    i = k+1

            return ans

        return F(0, len(S))

## Approach 2: Stack
class Solution3(object):
    def scoreOfParentheses(self, S):
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

if __name__ == "__main__":
    # a = Solution()
    # a.countOfAtoms("K4(ON(SO3)2)2")
    a = Solution()
    print(a.scoreOfParentheses("H2O"))
