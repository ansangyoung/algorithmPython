# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/
# https://leetcode.com/problems/factorial-trailing-zeroes/discuss/531121/leetcode-172-c-booksun 참조
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fiveCnt = 0
        while n:
            fiveCnt += n // 5
            n //= 5
        return fiveCnt
    testCase1 = 3
    testCase2 = 5
    testCase3 = 10
    print(trailingZeroes('', testCase1))
    print(trailingZeroes('', testCase2))
    print(trailingZeroes('', testCase3))