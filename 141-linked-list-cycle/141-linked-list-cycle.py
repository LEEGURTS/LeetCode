# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next if head else None
        while slow and fast:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
            
        return False