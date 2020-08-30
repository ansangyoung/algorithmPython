# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        resTmp = res
        l1EndFlg = False
        l2EndFlg = False
        while(1):
            cipher = 0
            if(l1):
                res.val += l1.val
                l1 = l1.next
                if(l1 == None):
                    l1EndFlg = True
            if(l2):
                res.val += l2.val
                l2 = l2.next
                if(l2 == None):
                    l2EndFlg = True
                
            if(res.val > 9):
                res.val %= 10
                cipher = 1
                
            if(l1 == None and l2 == None):
                if(cipher == 1):
                    resNext = ListNode()
                    resNext.val = cipher
                    res.next = resNext
                break
            elif(l2 != None):
                l2.val += cipher
            elif(l1 != None):
                l1.val += cipher
                
            if(l1EndFlg == False or l2EndFlg == False):
                resNext = ListNode()
                res.next = resNext
                res = res.next
            else:
                break
        '''
        while(1):
            print(resTmp.val)
            resTmp = resTmp.next
            if(resTmp == None):
                break
        '''
        return resTmp

testCase1_1 = ListNode()
testCase1_1.val = 2

testCase1_2 = ListNode()
testCase1_2.val = 4
testCase1_1.next = testCase1_2

testCase1_3 = ListNode()
testCase1_3.val = 3
testCase1_2.next = testCase1_3


testCase2_1 = ListNode()
testCase2_1.val = 5

testCase2_2 = ListNode()
testCase2_2.val = 6
testCase2_1.next = testCase2_2

testCase2_3 = ListNode()
testCase2_3.val = 4
testCase2_2.next = testCase2_3

testCase1 = Solution()
print(testCase1.addTwoNumbers(testCase1_1, testCase2_1))
