import heapq

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        q = []
        for person in people:
            heapq.heappush(q,(-person[0],person[1]))
        result = []

        while q:
            person = heapq.heappop(q)
            result.insert(person[1],[-person[0],person[1]])
        return result