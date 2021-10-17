class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        if needle == '':
            return 0

        for index in range(0, len(haystack)):
            if haystack[index:index + len(needle)] == needle:
                return index

        return 0


if __name__ == '__main__':
    print(Solution().strStr(haystack="hello", needle="ll"))
    print(Solution().strStr(haystack="abc", needle="c"))
