from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        closing_parentheses_map = {"}": "{", "]": "[", ")": "("}
        stack = deque()

        # If string has just 1 char or opening char is closing then return Failure
        if (len(s) == 1) or (s[0] in closing_parentheses_map.keys()):
            return False

        for char in s:
            # If stack is empty and next char is closing brace then return failure as closing brace
            # should only follow opening brace
            if len(stack) == 0 and char in closing_parentheses_map.keys():
                return False

            # For a closing brace char check if last char pushed to stack was a opening brace for this closing brace
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
    print(Solution().isValid(s="(){}}{"))
