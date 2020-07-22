# 46. Permutations
# https://leetcode.com/problems/permutations/
# https://medium.com/@hckcksrl/python-permutation-combination-a7bf9e5d6ab3 참조
from typing import List
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        permute = permutations(nums, numsLen)
        res = []
        for val in permute:
            res.append(list(val))
        return res
    testCase1 = [1,2,3]
    print(permute('', testCase1))