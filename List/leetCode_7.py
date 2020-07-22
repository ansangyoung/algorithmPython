# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        intToList = list(map(str, str(x)))
        intToList.reverse()
        if intToList[-1] == '-':
            intToList.insert(0, intToList.pop())
        while len(intToList) > 1 and intToList[-1] == '0':
            intToList.pop()
        ListToInt = int(''.join(intToList))
        maxInt = 2**31-1
        if  ListToInt < -maxInt-1 or maxInt < ListToInt:
            ListToInt = 0
        return ListToInt
    
    testCase1 = 123
    testCase2 = -123
    testCase3 = 120
    testCase4 = 0
    testCase5 = 1534236469
    print(reverse('', testCase1))
    print(reverse('', testCase2))
    print(reverse('', testCase3))
    print(reverse('', testCase4))
    print(reverse('', testCase5))