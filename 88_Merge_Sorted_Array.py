from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        prepend_values = None

        if m == 0 and n > 0:
            for index, value in enumerate(nums2):
                nums1[index] = nums2[index]
            return

        # Start from last index in nums1 to write the max value
        index_to_write = len(nums1) - 1
        nums1_index = m - 1
        nums2_index = n - 1

        while nums1_index >= 0 and nums2_index >= 0:
            nums1_value = nums1[nums1_index]
            nums2_value = nums2[nums2_index]

            if nums1_value >= nums2_value:
                value_to_write = nums1[nums1_index]
                nums1_index -= 1
            else:
                value_to_write = nums2[nums2_index]
                nums2_index -= 1

            nums1[index_to_write] = value_to_write
            index_to_write -= 1

        # Prepend remaining values
        if nums1_index >= 0:
            prepend_values = nums1[0:nums1_index + 1]
        elif nums2_index >= 0:
            prepend_values = nums2[0:nums2_index + 1]

        if prepend_values is not None:
            for index, value in enumerate(prepend_values):
                nums1[index] = value


if __name__ == '__main__':
    Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
    Solution().merge(nums1=[0], m=0, nums2=[1], n=1)
    Solution().merge(nums1=[2,0], m=1, nums2=[1], n=1)
