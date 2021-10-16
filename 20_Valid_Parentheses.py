from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        closing_parentheses_map = {"}": "{", "]": "[", ")": "("}
        stack = deque()

        if (len(s) == 1) or (s[0] in closing_parentheses_map.keys()):
            return False

        for char in s:
            if len(stack) == 0 and char in closing_parentheses_map.keys():
                return False

            if char in closing_parentheses_map.keys():
                last_element = stack.pop()
                if last_element != closing_parentheses_map[char]:
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # print(Solution().isValid(s="()"))
    # print(Solution().isValid(s = "()[]{}"))
    # print(Solution().isValid(s = "(]"))
    # print(Solution().isValid(s = "){"))
    print(Solution().isValid(s = "(){}}{"))
