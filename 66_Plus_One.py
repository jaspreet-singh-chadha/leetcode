from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 9:
            new_digits = [0] + digits
        else:
            new_digits = digits

        # So that 1 is added first time in ones place
        carryover = 1
        for index in range(len(new_digits) - 1, -1, -1):
            if carryover == 1:
                if new_digits[index] == 9:
                    new_digits[index] = 0
                    carryover = 1
                else:
                    new_digits[index] = new_digits[index] + 1
                    carryover = 0

        if new_digits[0] == 0:
            return new_digits[1:]
        else:
            return new_digits


if __name__ == '__main__':
    print(Solution().plusOne(digits=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
