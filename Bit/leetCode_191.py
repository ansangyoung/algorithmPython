# https://leetcode.com/problems/number-of-1-bits/
# problem 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n //= 2
        return res
    
    #print(hammingWeight("", int('00000000000000000000000000001011', 2)))
    #print(hammingWeight("", int('00000000000000000000000010000000', 2)))
    #print(hammingWeight("", int('11111111111111111111111111111101', 2)))