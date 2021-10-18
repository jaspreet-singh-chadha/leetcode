from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the smallest length string in the passed list
        smallest_str = self.get_smallest_string_from_list(strs_list=strs)
        max_substring = ''
        str_seq_to_find = ''

        # Check for existence of chars from smallest list element in rest of the elements
        for char in smallest_str:
            str_seq_to_find = str_seq_to_find + char
            char_found_in_all_elements = True
            for element in strs:
                if str_seq_to_find not in element:
                    char_found_in_all_elements = False
                    str_seq_to_find = ''
                    break
            if char_found_in_all_elements is True:
                if len(str_seq_to_find) > len(max_substring):
                    max_substring = str_seq_to_find

        return max_substring

    def get_smallest_string_from_list(self, strs_list) -> str:
        min_length = None
        min_length_string = ''

        for element in strs_list:
            if min_length is None or len(element) < min_length:
                min_length_string = element

        return min_length_string


if __name__ == '__main__':
    # print(Solution().longestCommonPrefix(strs=["flower","flow","flight"]))
    # print(Solution().longestCommonPrefix(strs=["dog","racecar","car"]))
    print(Solution().longestCommonPrefix(strs=["reflower","flow","flight"]))