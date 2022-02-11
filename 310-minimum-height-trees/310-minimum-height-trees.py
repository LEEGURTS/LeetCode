class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        while n > 2:
            remove = []
            for i in graph:
                if len(graph[i]) == 1:
                    remove.append(i)
                
            for k in remove:
                
                graph[graph[k][0]].remove(k)
                del graph[k]
            n -= len(remove)
        return graph.keys()
