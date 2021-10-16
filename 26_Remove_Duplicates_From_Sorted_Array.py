from typing import List
from collections import deque

# Return k after placing the final result in the first k slots of nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        empty_indices = deque()
        duplicate_count = 0

        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                empty_indices.append(index)
                duplicate_count += 1
            elif len(empty_indices) > 0:
                index_to_write = empty_indices.popleft()
                nums[index_to_write] = nums[index]
                # Now this index is empty as it has been copied to another index
                empty_indices.append(index)

        return len(nums) - duplicate_count


if __name__ == '__main__':
    print(Solution().removeDuplicates(nums=[1, 1, 2, 3]))
