import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        q = collections.deque()

        for i,n in enumerate(nums):
            if q and i - q[0] == k:
                q.popleft()
            while q and n > nums[q[-1]]:
                q.pop()
            q.append(i)

            if i >= k-1:
                result.append(nums[q[0]])
        return result