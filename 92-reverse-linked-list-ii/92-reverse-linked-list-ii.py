# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        for i in  range(left - 1):
            start = start.next
        end = start.next

        for i in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        return root.next