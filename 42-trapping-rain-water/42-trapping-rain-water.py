class Solution:
    def trap(self, height: list[int]) -> int:
        mid = height.index(max(height))
        left, right, count = mid-1, mid+1, 0

        while left >= 0:
            count += max(height[0:left+1])-height[left]
            left-=1
        while right < len(height):
            count += max(height[right:len(height)]) - height[right]
            right+=1
        return count
