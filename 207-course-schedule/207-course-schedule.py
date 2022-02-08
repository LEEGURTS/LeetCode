class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()
        
        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            
            
            traced.add(i)
            for k in graph[i]:
                if not dfs(k):
                    return False
            traced.remove(i)
            visited.add(i)
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
            
        return True