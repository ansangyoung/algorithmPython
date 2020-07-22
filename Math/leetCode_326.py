# 326. Power of Three
# https://leetcode.com/problems/power-of-three/
# http://leetcode0.blogspot.com/2016/01/326-power-of-three.html 참조
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = False
        if n > 0:
            exponent = math.log(n)/math.log(3)
            if pow(3, round(exponent)) == n:
                res = True
        return res

    testCase = [27, 9, 45, 243, 0]
    for val in testCase:
        print(isPowerOfThree('', val))