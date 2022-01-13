# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)


    def addTwoNumbers(self, l1, l2) -> ListNode:
        root = cur = ListNode(0)
        flag = 0
        while l1 or l2 or flag:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            flag, val = divmod(sum+flag,10)
            cur.next = ListNode(val)
            cur = cur.next
        return root.next
    
            
        