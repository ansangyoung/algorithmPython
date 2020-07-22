# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# + ?��?�� 존재?��?�� 문자�? 1�? ?��??? �? ?��?�� 반복?��?�� 문자�? 찾을 ?�� ?��?��?��?��?��.
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        resFlg = True
        replaceStr = ("".join(re.findall("[a-zA-Z0-9]+", s))).lower()
        print(replaceStr)
        replaceStrLen = len(replaceStr)
        replaceStrLenHalf = replaceStrLen // 2
        for i in range(0, replaceStrLenHalf):
            if(replaceStr[i] != replaceStr[replaceStrLen - 1 - i]):
                resFlg = False
                break
        
        return resFlg

    testCase1 = 'A man, a plan, a canal: Panama'
    testCase2 = 'race a car'
    testCase3 = '0P'
    print(isPalindrome('', str(testCase1)))
    print(isPalindrome('', str(testCase2)))
    print(isPalindrome('', str(testCase3)))