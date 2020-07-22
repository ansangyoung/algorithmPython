# 198. House Robber
# https://leetcode.com/problems/house-robber/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        numsLen = len(nums)
        res = 0
        if numsLen == 1:
            res = nums[0]
        elif numsLen >= 2:
            res1 = nums[1]
            res2 = nums[0]
            for i in range(2, numsLen):
                print(i, res1, res2, res2 + nums[i])
                res = max(res1, res2 + nums[i])
                res2 = max(res1, res2)
                res1 = max(res, res1)
            res = max(res1, res2)
        return res
    
    testCase1 = [1,2,3,1]
    testCase2 = [2,7,9,3,1]
    testCase3 = [2,1,1,2]
    testCase4 = [2,1,1,3,1,1,3]
    print(rob('', testCase1))
    print(rob('', testCase2))
    print(rob('', testCase3))
    print(rob('', testCase4))
