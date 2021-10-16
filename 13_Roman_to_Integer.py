class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        precursor_group_map = {"V": "I", "X": "I",
                               "L": "X", "C": "X",
                               "D": "C", "M": "C"}

        last_char = s[0]
        numeral_value = roman_to_numeral_map[last_char]

        for char in s[1:len(s)]:
            if char in precursor_group_map.keys() and last_char == precursor_group_map[char]:
                numeral_value = numeral_value + (roman_to_numeral_map[char] - 2 * roman_to_numeral_map[last_char])
            else:
                numeral_value = numeral_value + roman_to_numeral_map[char]
            last_char = char

        return numeral_value




if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))