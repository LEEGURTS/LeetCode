import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = collections.Counter(nums)
        return count.most_common(1)[0][0]
