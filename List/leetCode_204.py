# 204. Count Primes
# https://leetcode.com/problems/count-primes/
# https://brownbears.tistory.com/445 ?—?¼?† ?Š¤?…Œ?„¤?Š¤?˜ ì²? ì°¸ì¡°
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        nMin = 2
        nMax = math.ceil(math.sqrt(n))
        isPrimes = [True] * n
        for i in range(nMin, nMax):
            if isPrimes[i]:
                for j in range(i+i, n, i):
                    isPrimes[j] = False
        res = len([i for i in range(nMin, n) if isPrimes[i]])
        return res
    testCase1 = 10
    print(countPrimes('', testCase1))