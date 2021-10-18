import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = False

        # Strip all non alphabets chars
        temp = re.split("[^a-zA-Z0-9]", s)
        stripped_str = ''.join(temp)

        result = self.check_palindrome_string(stripped_str.lower())

        return result

    def check_palindrome_string(self, s):
        start_index = 0
        end_index = len(s) - 1

        while start_index < end_index:
            if s[start_index] != s[end_index]:
                return False
            start_index += 1
            end_index -= 1

        return True


if __name__ == '__main__':
    # print(Solution().isPalindrome("This, is: Sparta"))
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome("0P"))
