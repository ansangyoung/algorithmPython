# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Len = len(nums1)
        for i in range(nums1Len-m, 0, -1):
            del nums1[-1]

        v1 = 0
        v2 = 0
        while v1 < m:
            if v2 < n and nums2[v2] <= nums1[v1]:
                nums1.insert(v1, nums2[v2])
                v2 += 1
            else:
                v1 += 1
                
        while v2 < n:
            if 0 < v1 and nums2[v2] <= nums1[v1-1]:
                nums1.insert(v1-1, nums2[v2])
                v2 += 1
            elif v1 == len(nums1):
                nums1.insert(len(nums1), nums2[v2])
                v2 += 1
            else:
                v1 += 1
                
    testCase1 = [1,2,3,0,0,0]
    testCase2 = [2,5,6]
    merge('', testCase1, 3, testCase2, 3)
    testCase1 = [2,0]
    testCase2 = [1]
    merge('', testCase1, 1, testCase2, 1)
    testCase1 = [1]
    testCase2 = []
    merge('', testCase1, 1, testCase2, 0)
    testCase1 = [0]
    testCase2 = [1]
    #merge('', testCase1, 0, testCase2, 1)
    testCase1 = [4,5,6,0,0,0]
    testCase2 = [1,2,3]
    merge('', testCase1, 3, testCase2, 3)
    testCase1 = [4,0,0,0,0,0]
    testCase2 = [1,2,3,5,6]
    merge('', testCase1, 1, testCase2, 5)
    testCase1 = [1,5,8,0,0,0,0,0]
    testCase2 = [-1,2,2,4,6]
    merge('', testCase1, 3, testCase2, 5)