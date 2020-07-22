# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        k %= numsLen
        #nums = nums[numsLen-k : numsLen] + nums[0 : numsLen-k]
        for i in range(k):
            nums.insert(0, nums.pop())
        
        print(nums)
        return(nums)
        
    testNums1 = [1,2,3,4,5,6,7]
    testK1 = 3
    testNums2 = [-1,-100,3,99]
    testK2 = 2
    print(rotate('', testNums1, testK1))
    print(rotate('', testNums2, testK2))