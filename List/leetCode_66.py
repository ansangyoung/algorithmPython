#66. Plus One
#https://leetcode.com/problems/plus-one/

class Solution:
    #def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        lstToInt = 0
        digitsLen = len(digits)
        cipher = 0
        for i in range(digitsLen-1, -1, -1):
            lstToInt += (digits[i] * (10 ** cipher))
            cipher += 1
        lstToInt += 1
        intToLst = []
        while(lstToInt > 0):
            intToLst.append(lstToInt % 10)
            lstToInt //= 10
        intToLst.reverse()
        return intToLst
    testCase1 = [1,2,3]
    testCase2 = [4,3,2,1]
    print(plusOne('', testCase1))
    print(plusOne('', testCase2))