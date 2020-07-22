# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/
import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        resInfo = re.search(needle, haystack)
        res = resInfo.start() if resInfo else -1
        return res
    
    haystack = "hello"
    needle = "ll"
    print(strStr("", haystack, needle))
    haystack = "aaaaa"
    needle = "bba"
    print(strStr("", haystack, needle))