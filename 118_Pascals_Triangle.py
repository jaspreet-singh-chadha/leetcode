from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]

        for numRow in range(3, numRows + 1):
            last_row = result[numRow - 2]
            # Start the row with 1 since first element in a row has only 1 parent i.e 1
            row = [1]
            for index in range(0, len(last_row) - 1):
                sum = last_row[index] + last_row[index + 1]
                row.append(sum)
            # End the row with 1 since last element in a row has only 1 parent i.e 1
            row.append(1)
            result.append(row)

        return result


if __name__ == '__main__':
    print(Solution().generate(numRows=7))
