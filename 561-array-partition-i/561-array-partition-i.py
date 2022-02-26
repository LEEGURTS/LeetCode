class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(1,len(nums)//2+1):
            result += nums[-2*i]
        return result