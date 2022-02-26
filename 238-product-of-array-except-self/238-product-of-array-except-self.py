class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_right = [1]
        right_left = [1]
        result = []
        length = len(nums)
        for i in range(length-1):
            left_right.append(left_right[i] * nums[i])
            right_left.append(right_left[i] * nums[-(i+1)])

        for i in range(length):
            result.append(left_right[i]*right_left[-(i+1)])
        return result