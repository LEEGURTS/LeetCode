class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        result.append([])
        def dfs(idx=0,fin = []):
            if idx == len(nums):
                return
            for i in range(idx,len(nums)):
                fin.append(nums[i])
                result.append(fin[:])
                dfs(i+1,fin)
                fin.remove(nums[i])
        dfs()
        return result