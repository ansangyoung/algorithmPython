#https://leetcode.com/problems/missing-number/submissions/
#problem 268. Missing Number
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        aLen = len(nums)
        resFlg = False
        for val in range(0, aLen):
            if val in nums:
                continue
            else:
                res = val
                resFlg = True
                break
        if resFlg != True:
            res = aLen
        return res
    testCase1 = [3,0,1]
    print(missingNumber('', testCase1))