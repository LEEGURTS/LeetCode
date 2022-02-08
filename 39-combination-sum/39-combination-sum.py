class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(start, fin=[]):
            if sum(fin) == target:
                result.append(fin[:])
                return
            elif sum(fin) > target:
                return
            for i in range(start, len(candidates)):
                if sum(fin) < target:
                    fin.append(candidates[i])
                    dfs(i,fin)
                    fin.remove(candidates[i])
        dfs(0)
        return result