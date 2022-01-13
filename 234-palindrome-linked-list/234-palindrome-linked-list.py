# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        record = None
        while fast and fast.next:
            fast = fast.next.next
            record, record.next, slow = slow, record, slow.next
        if fast:
            slow = slow.next
        while record and record.val == slow.val:
            slow, record = slow.next, record.next
        
        return not record
        