class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def dfs(choose:list, start):
            result.append(choose[:])
            for i in range(start,len(nums)):
                dfs(choose+[nums[i]], i+1)
        dfs([],0)
        return result
    