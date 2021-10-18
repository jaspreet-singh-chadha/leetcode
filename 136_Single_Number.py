from typing import List

"""
The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence. 
The idea is based on the following two facts. 
a) XOR of a number with itself is 0. 
b) XOR of a number with 0 is number itself.

Let us consider the above example.  
Let ^ be xor operator as in C and C++.

res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

Since XOR is associative and commutative, above 
expression can be written as:
res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
    = 7 ^ 0 ^ 0 ^ 0
    = 7 ^ 0
    = 7 
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


if __name__ == '__main__':
    print(Solution().singleNumber(nums=[1,1,2,3,2,3,4,5,5,6,7,6,7]))
    print(Solution().singleNumber(nums=[2, 3, 5, 4, 5, 3, 4]))
