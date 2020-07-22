# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# https://daimhada.tistory.com/126 참조
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        tmp = list(set(nums))
        tmp.sort()
        tmpLen = len(tmp)
        for i, val in enumerate(tmp):
            nums[i] = val
            if(i == tmpLen -1):
                break
        '''
        nums.sort()
        numsLen = len(nums)
        res = 1
        for numsIdx in range(1, numsLen):
            if nums[numsIdx - 1] != nums[numsIdx]:
                nums[res] = nums[numsIdx]
                res = res + 1
        return res
    testCase1 = [1,1,2]
    testCase2 = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates('', testCase1))
    print(removeDuplicates('', testCase2))