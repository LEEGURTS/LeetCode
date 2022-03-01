class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        data = collections.Counter(nums).most_common(k)
        return list(d[0] for d in data)
