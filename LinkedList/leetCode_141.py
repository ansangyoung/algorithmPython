# 38. Count and Say
# https://leetcode.com/problems/count-and-say/
# https://itdar.tistory.com/entry/LeetCode-141-LinkedListCycle-Algorithm 참조
# https://allo-ew.tistory.com/96 참조

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        resFlg = False
        turtle = head
        rabbit = head.next if head else None
        while(turtle and rabbit):
            if(turtle == rabbit):
                resFlg = True
                break
            turtle = turtle.next
            rabbit = rabbit.next.next if rabbit.next else None
            
        return resFlg