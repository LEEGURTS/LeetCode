import collections
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))

        Q = [(0, k)]
        dist = collections.defaultdict(list)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q,(alt, v))
        
        if len(dist) == n:
            return max(dist.values())
        return -1



