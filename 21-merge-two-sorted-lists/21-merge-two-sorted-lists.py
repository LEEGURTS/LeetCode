# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = cur = ListNode()
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    value=l1.val
                    l1=l1.next
                else:
                    value=l2.val
                    l2=l2.next
            elif l1:
                value = l1.val
                l1 = l1.next
            elif l2:
                value = l2.val
                l2 = l2.next
            cur.next=ListNode(value)
            cur=cur.next
        root=root.next
        return root
            

        