# 78. Subsets
# https://leetcode.com/problems/subsets/
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        zeroSet = []
        resSet = []
        resSet.insert(0, zeroSet)
        
        numsIdx = 0
        numsLen = len(nums)
        
        while numsIdx < numsLen:
            accumulatedSet =[]
            for element in resSet:
                # 기존 원소
                accumulatedSet.append([e for e in element])
                # 원소 + 현시점 원소
                accumulatedSet.append([e for e in element] + [nums[numsIdx]])
            numsIdx += 1
            resSet = accumulatedSet
        return resSet
