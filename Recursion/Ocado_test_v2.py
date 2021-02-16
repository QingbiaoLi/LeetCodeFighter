# A Python program to remove "b" and 'ac' from input string
# def solution(S):
#     # write your code in Python 3.6
#     # Try to debug on my own IDE
#
#     chars = list(S)
#     char_prev = ''
#
#     checkStatus = find_adj(S[0],char_prev)
#
#     while checkStatus
#     for char_cur in s:
#
#
#
# def find_adj(char_cur, char_prev):
#     if char_cur+char_prev in ['AB','BA','CD','DC']:
#         return ''
#     else:
#         return char_cur+char_prev
#
#
#
# def removeDuplicates(s):
#     chars = list(s)
#     prev = None
#     k = 0
#
#     for c in s:
#         if prev != c:
#             chars[k] = c
#             prev = c
#             k = k + 1
#
#     return ''.join(chars[:k])


# Function to remove all occurrences of "AB" and "C" from the string
def remove(chars):
    # i maintains the position of current in the input string
    i = 0

    # k maintains the next free position in output string
    k = 0

    # do till we reach the end of the string
    while i < len(str):

        # if current is 'B' and previous (need not
        # be adjacent) was 'A', increment i and decrement k
        if chars[i] == 'B' and (k > 0 and chars[k - 1] == 'A'):
            k = k - 1
            i = i + 1
        elif chars[i] == 'A' and (k > 0 and chars[k - 1] == 'B'):
            k = k - 1
            i = i + 1

        elif chars[i] == 'C' and (k > 0 and chars[k - 1] == 'D'):
            k = k - 1
            i = i + 1

        elif chars[i] == 'D' and (k > 0 and chars[k - 1] == 'C'):
            k = k - 1
            i = i + 1


        # for any other character, increment both i and k
        else:
            chars[k] = chars[i]
            k = k + 1
            i = i + 1

    return ''.join(chars[:k])


if __name__ == '__main__':
    str = "ACBDACBD"

    str = remove(list(str))
    print(str)
    print('After removal of "AB" and "C" is {}'.format(str))


# if __name__ == '__main__':
#     s = "CBACD"
#
#     s = solution(s)
#     print(s)


# def removeDuplicates(self, s, k):
#     size = len(s)
#     if k > size or not k: return s
#     stack = []
#     for c in s:
#         if stack and stack[-1][0] == c:
#             stack[-1][1] += 1
#             if stack[-1][1] == k: stack.pop()
#             continue
#         stack.append([c, 1])
#     res = ''
#     for value, count in stack:
#         res += value * count
#     return res

#
#
# def reduceString(s, l):
#     count = 1
#     steps = 0
#
#     # traverse in
#     # the string
#     for i in range(1, l):
#         # if adjacent
#         # characters are same
#         if (s[i] is s[i - 1]):
#             count += 1
#
#         else:
#             # if same adjacent pairs
#             # are more than 1
#             steps += (int)(count / 2)
#
#             count = 1
#         steps += (int)(count / 2)
#     return steps
#
#
# # Driver Code
s = "cbaacd"
#
# l = len(s)
# print(reduceString(s, l))
#
# # # Driver program
# string1 = solution(s)
# print(string1)


# class Solution2(object):
#     def decodeString(self, s):
#         num = 0
#         string = ''
#         stack = []
#         for c in s:
#             if c.isdigit():
#                 num = num * 10 + int(c)
#             elif c == "[":
#                 stack.append(string)
#                 stack.append(num)
#                 string = ''
#                 num = 0
#             elif c.isalpha():
#                 string += c
#             elif c == ']':
#                 pre_num = stack.pop()
#                 pre_string = stack.pop()
#                 string = pre_string + pre_num * string
#         return string