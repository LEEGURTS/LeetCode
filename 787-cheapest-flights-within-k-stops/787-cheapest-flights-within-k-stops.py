import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))
        howmany = 0
        visit = {}
        Q = [(0, src, howmany)]
        while Q:
            price, node , howmany= heapq.heappop(Q)
            if node == dst:
                return price
            if node not in visit or visit[node] > howmany:
                visit[node] = howmany
                if howmany <= k:
                    for v,w in graph[node]:
                        alt =price+w
                        heapq.heappush(Q,(alt,v,howmany+1))
        return -1