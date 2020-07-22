# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        res = int(math.sqrt(x))
        return res
    
    testCase1 = 4
    testCase2 = 8
    print(mySqrt('', testCase1))
    print(mySqrt('', testCase2))