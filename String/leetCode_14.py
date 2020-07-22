# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strsLen = len(strs)
        if strsLen > 0:
            strFirstLen = len(strs[0])
            compFlg = True
            for i in range(0, strFirstLen):
                if i < strFirstLen:
                    currCompStr = strs[0][i]
                    for s in strs:
                        if len(s) <= i or currCompStr != s[i]:
                            compFlg = False
                            break
                else:
                    compFlg = False
                if compFlg == False:
                    break
                res += currCompStr
        return res

    testCase1 = ["flower","flow","flight"]
    testCase2 = ["dog","racecar","car"]
    testCase3 = ["abca","abc"]
    print(longestCommonPrefix('', testCase1))
    print(longestCommonPrefix('', testCase2))
    print(longestCommonPrefix('', testCase3))