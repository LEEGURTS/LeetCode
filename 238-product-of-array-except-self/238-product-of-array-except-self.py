class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        allp = 1
        result = []
        for num in nums:
            allp *= num
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = 1
                for j in range(len(nums)):
                    if j != i:
                        temp *= nums[j]
                result.append(temp)
            else:
                result.append(allp//nums[i])
        return result