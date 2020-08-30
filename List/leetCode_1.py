# 1. Two Sum
# https://leetcode.com/problems/two-sum/
from typing import List
class Solution:
    def __init__(self):
        self.nums = []
        self.target = 0
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        res = []
        resFlg = False
        for i in range(numsLen):
            for j in range(i + 1, numsLen):
                if(nums[i] + nums[j] == target):
                    resFlg = True
                    res.insert(0, i)
                    res.insert(1, j)
                    break
            if(resFlg):
                break
        return res

testCase1 = Solution()
testCase1.nums = [2,7,11,15]
testCase1.target = 9
print(testCase1.twoSum(testCase1.nums, testCase1.target))

testCase2 = Solution()
testCase2.nums = [3,2,4]
testCase2.target = 6
print(testCase2.twoSum(testCase2.nums, testCase2.target))

testCase3 = Solution()
testCase3.nums = [3,3]
testCase3.target = 6
print(testCase3.twoSum(testCase3.nums, testCase3.target))
