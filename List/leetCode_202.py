#https://leetcode.com/problems/happy-number/
#problem 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        res = False
        loopEscape = False
        accLst = []
        accLst.append(n)
        while(1):
            print(n)
            if res == False:
                strN = str(n)
                n = 0
                for s in strN:
                    n += int(s) * int(s)
                if n == 1:
                    res = True
                    break
                
                for val in accLst:
                    if val == n:
                        res = False
                        loopEscape = True
                        break
                if loopEscape:
                    break
                accLst.append(n)
        return res
    #print(isHappy("", 19))
    #print(isHappy("", 2))