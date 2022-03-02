class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(index, summation, path: list[int]):
            if summation > target:
                return
            if summation == target:
                result.append(path[:])

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, summation + candidates[i], path)
                path.pop()

        dfs(0, 0, [])
        return result