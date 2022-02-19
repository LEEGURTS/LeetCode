
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeList(l1,l2):
            if l1 and l2:
                if l1.val > l2.val:
                    l1,l2 = l2,l1
                l1.next = mergeList(l1.next,l2)
            
            return l1 or l2

        def mergeSort(node):
            if not (node and node.next):
                return node
            half, slow, fast = None, node, node

            while fast and fast.next:
                half, slow, fast = slow, slow.next, fast.next.next
            half.next = None

            l1 = mergeSort(node)
            l2 = mergeSort(slow)

            return mergeList(l1,l2)
        
        return mergeSort(head)