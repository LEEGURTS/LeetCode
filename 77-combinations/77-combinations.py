class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        nums = list(range(1,n+1))
        def dfs(choose: list,start):
            if len(choose) == k:
                result.append(choose[:])
            for i in range(start,n):
                dfs(choose+[nums[i]],i+1)
        dfs([],0)
        return result
                
