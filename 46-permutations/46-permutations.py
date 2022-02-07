class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        temp=[]
        def dfs(fin: list[int], number: list[int]):
            if len(number) == 0:

                result.append(fin[:])
                return
            for i in range(len(number)):
                copy_list = number[:]
                fin.append(number[i])

                copy_list.remove(number[i])
                dfs(fin, copy_list)
                fin.remove(number[i])
        dfs(temp, nums)
        return result