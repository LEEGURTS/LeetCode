import collections


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        data = collections.defaultdict(int)
        for i,value in enumerate(nums):
            data[value] = i
        for i,value in enumerate(nums):
            if target - value in data and i != data[target-value]:
                return [i,data[target-value]]