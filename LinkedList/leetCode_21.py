class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
https://somjang.tistory.com/entry/leetCode-21-Merge-Two-Sorted-Lists [?†œ?”¨ì¢‹ì???ž¥?”¨] ì°¸ê³ 
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        my_l1 = []
        
        while l1 != None:
            my_l1.append(int(l1.val))
            l1 = l1.next
            
        while l2 != None:
            my_l1.append(int(l2.val))
            l2 = l2.next

        my_l1 = list(sorted(my_l1))

        answerList = None

        for i in range(len(my_l1)):
            if i == 0:
                answerList = ListNode(my_l1[i])
            else:
                new_node = ListNode(my_l1[i])
                currNode = answerList
                while currNode.next != None:
                    currNode = currNode.next
                currNode.next = new_node
        return answerList
    '''
    s1 = ListNode(1)
    s1.next = ListNode(3)
    s2 = ListNode(1)
    s2.next = ListNode(2)
    tmpListNode = mergeTwoLists("", s1, s2)
    tmpList = []
    while tmpListNode != None:
        tmpList.append(int(tmpListNode.val))
        tmpListNode = tmpListNode.next
    print(tmpList)
    '''