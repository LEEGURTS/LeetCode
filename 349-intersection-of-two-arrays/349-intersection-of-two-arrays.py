import bisect


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2.sort()
        result = set()
        for i in nums1:
            temp = bisect.bisect_left(nums2,i)
            if temp < len(nums2) and nums2[temp] == i:
                result.add(i)
        return result