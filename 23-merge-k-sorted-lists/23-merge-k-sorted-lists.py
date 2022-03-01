import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q,(lists[i].val,i,lists[i]))

        root = result = ListNode()
        while q:
            node = heapq.heappop(q)
            if node[2]:
                root.next = node[2]
            if node[2].next:
                heapq.heappush(q,(node[2].next.val,node[1],node[2].next))
            root = root.next
        return result.next