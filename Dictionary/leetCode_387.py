class Solution:
    '''
    def firstUniqChar(self, s: str) -> int:
        strToList = list(s)
        strToListLen= len(strToList)
        sameCnt = 0
        
        for i in range(0, strToListLen):
            if(strToList.count(strToList[i]) == 1):
                return i
        return -1
    '''
    '''
        http://www.goodtecher.com/leetcode-387-first-unique-character-in-a-string/ 참고
    '''
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] = counter[char] + 1
                
        for i, char in enumerate(s):
            #print(i, char, enumerate(s))
            if counter[char] == 1:
                return i
            
        return -1
    #print(firstUniqChar("", "leetcode"))
    #print(firstUniqChar("", "loveleetcode"))