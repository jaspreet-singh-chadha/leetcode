from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums_map.keys():
                return [index, nums_map[diff]]
            else:
                nums_map[num] = index

        return []

if __name__ == '__main__':
    print(Solution().twoSum([1,2,3,4], 7))
