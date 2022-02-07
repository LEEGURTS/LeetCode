class Solution:
    def topKFrequent(self,nums: list[int], k: int) -> list[int]:
        data = collections.Counter(nums).most_common(k)
        result = []
        for temp in data:
            result.append(temp[0])
        return result
        