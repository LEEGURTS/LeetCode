
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = pred = ListNode()
        pred.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
                
            head = head.next
        return root.next
            