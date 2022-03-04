class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(choose:list,start):
            summation = sum(choose)
            if summation > target:
                return
            if summation == target:
                result.append(choose)
                return
            for i in range(start,len(candidates)):
                dfs(choose + [candidates[i]], i)
        dfs([],0)
        return result