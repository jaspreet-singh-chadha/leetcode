class Solution:

    def is_palindrome(self, str):
        result = True
        if len(str) == 1:
            return result

        forward_index = 0
        reverse_index = len(str) - 1

        while forward_index < reverse_index:
            if str[forward_index] != str[reverse_index]:
                result = False
                break
            forward_index += 1
            reverse_index -= 1

        return result

    def get_palindrome_strings(self, str_to_search, starting_ending_char_of_palin_substr):
        palindrome_strings = []
        for index in range(len(str_to_search)):
            if str_to_search[index] == starting_ending_char_of_palin_substr:
                palin_substring = starting_ending_char_of_palin_substr + str_to_search[0:index + 1]
                if self.is_palindrome(palin_substring):
                    palindrome_strings.append(palin_substring)

        return palindrome_strings

    def get_palindrome_strings_V1(self, str_to_search, starting_ending_char_of_palin_substr,
                                  max_palindrome_string_so_far):
        palindrome_strings = []
        for index in range(len(str_to_search)):
            if str_to_search[index] == starting_ending_char_of_palin_substr:
                palin_substring = starting_ending_char_of_palin_substr + str_to_search[0:index + 1]
                if len(palin_substring) > len(max_palindrome_string_so_far):
                    if self.is_palindrome(palin_substring):
                        max_palindrome_string_so_far = palin_substring

        return max_palindrome_string_so_far

    def get_palindrome_str_of_max_size(self, palin_list: list):
        max_str_size = 0
        max_size_palin_str = None
        for palin_str in palin_list:
            palin_str_size = len(palin_str)
            if palin_str_size > max_str_size:
                max_str_size = palin_str_size
                max_size_palin_str = palin_str
        return max_size_palin_str, max_str_size

    def is_perfect_palindrome(self, palindrome_str):
        str_to_check_length = len(palindrome_str)
        result = False

        if (str_to_check_length % 2) == 0:
            half_index = int(str_to_check_length / 2)
        else:
            half_index = int((str_to_check_length - 1) / 2)

        tail_str = palindrome_str[half_index + 1:]
        # reversed_tail_str = tail_str[::-1]
        head_str = palindrome_str[:half_index]

        if head_str == tail_str:
            result = True

        return result

    def is_half_palindrome(self, palindrome_str):
        str_to_check_length = len(palindrome_str)
        result = False

        if (str_to_check_length % 2) == 0:
            half_index = int(str_to_check_length / 2)
        else:
            half_index = int((str_to_check_length - 1) / 2)

        tail_str = palindrome_str[half_index:]
        # reversed_tail_str = tail_str[::-1]
        head_str = palindrome_str[:half_index]

        if (len(head_str) == len(tail_str)) and (len(set(head_str)) == 1) and (len(set(tail_str)) == 1):
            result = True

        return result, list(set(head_str))[0]

    def longestPalindrome(self, str_to_check):

        str_to_check_length = len(str_to_check)
        palindrome_sub_strings = []
        max_palindrome_string_so_far = ''
        test = len(set(str_to_check))

        if (len(set(str_to_check)) == 1) or (self.is_perfect_palindrome(palindrome_str=str_to_check)):
            return str_to_check

        is_half_palindrome, half_palindrome_str = self.is_half_palindrome(palindrome_str=str_to_check)

        if is_half_palindrome:
            return half_palindrome_str

        for index in range(str_to_check_length):
            palin_str_starting_ending_char = str_to_check[index]
            remaining_str = str_to_check[index + 1: str_to_check_length + 1]
            max_palindrome_string_so_far = self.get_palindrome_strings_V1(str_to_search=remaining_str,
                                                                          starting_ending_char_of_palin_substr=palin_str_starting_ending_char,
                                                                          max_palindrome_string_so_far=max_palindrome_string_so_far)
        if max_palindrome_string_so_far == '':
            biggest_palindrome_substring = str_to_check[0]
        else:
            biggest_palindrome_substring = max_palindrome_string_so_far

        return biggest_palindrome_substring


if __name__ == '__main__':
    print(Solution().longestPalindrome(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
