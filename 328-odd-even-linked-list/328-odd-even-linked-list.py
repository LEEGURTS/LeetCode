# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        start = oddNode = ListNode()
        start2 = evenNode = ListNode()
        isodd = 1
        while head:
            if isodd:
                oddNode.next = head
                oddNode = oddNode.next
                isodd = 0
            else:
                evenNode.next = head
                evenNode = evenNode.next
                isodd = 1
            head = head.next
        evenNode.next = None
        oddNode.next = start2.next
        return start.next