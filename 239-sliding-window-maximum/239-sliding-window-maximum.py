class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = collections.deque()
        
        l = 0
        for i in range(len(nums)):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            
            if l > window[0]:
                window.popleft()
            
            if i + 1 >= k:
                res.append(nums[window[0]])
                l += 1
        
        return res