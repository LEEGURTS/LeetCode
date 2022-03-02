class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(number: list[int], fin: list[int]):
            if not number:
                result.append(fin[:])
                return
            for i in range(len(number)):
                copy_list = number[:]
                fin.append(number[i])
                copy_list.remove(number[i])
                dfs(copy_list,fin)
                fin.remove(number[i])

        dfs(nums, [])
        return result