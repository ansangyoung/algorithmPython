# 38. Count and Say
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        initStr = '11'
        initStrLen = len(initStr)
        resStr = ''
        cnt = 1
        for i in range(2, n):
            resStr = ''
            for j in range(0, initStrLen):
                if j < initStrLen-1 and initStr[j] != initStr[j+1]:
                    resStr = resStr + str(cnt) + initStr[j]
                    cnt = 1
                elif j == initStrLen-1:
                    resStr = resStr + str(cnt) + initStr[j]
                    cnt = 1
                else:
                    cnt = cnt + 1
            initStr = resStr
            initStrLen = len(initStr)
        if n < 3:
            resStr = initStr[0:n]
        return resStr
    
    testCase = [1, 2, 3, 4, 5]
    for val in testCase:
        print(countAndSay('', val))