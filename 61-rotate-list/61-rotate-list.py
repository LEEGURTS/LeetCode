
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        start = head
        prev = head
        if k%length == 0:
            return head
        toggle = 0
        for i in range(length-(k%length)):
            prev = start
            start = start.next
            toggle = 1
        if toggle == 1:
            prev.next = None
            node.next = head

        return start
