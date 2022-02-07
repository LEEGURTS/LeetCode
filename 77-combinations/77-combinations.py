class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = list(range(1, n+1))
        result = []
        temp = []

        def dfs(fin: list[int], number: list[int]):
            if len(fin) == k:
                result.append(fin[:])
                return
            copy_list = number[:]
            for i in range(len(number)):
                fin.append(number[i])
                copy_list.remove(number[i])
                dfs(fin, copy_list)
                fin.remove(number[i])
        dfs(temp,nums)
        return result
