class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()
        left, right = 0, len(nums)-1
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.add((nums[i],nums[left],nums[right]))
                    right -=1
                    left += 1
        return result
                    